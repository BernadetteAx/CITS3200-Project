// =====================================================================
// RESULTS_TOUR.JS — "?" spotlight tour for the Game Results page
// =====================================================================
//
// When the player presses the "?" button, one spotlight glides through
// four existing panels, then fades out:
//
//     FINAL SCORE -> MISSION ACHIEVEMENT -> MISSION RESULTS -> ITEM INVENTORY
//
// DESIGN NOTES FOR REVIEWERS
//
// 1. Presentation only. Nothing here reads, changes or re-emits result
//    data. result_page.js and result_achievement.js are not modified and
//    still render everything exactly as before.
//
// 2. One scrim, one spotlight, one coach mark, one controller. They are
//    built once per run and reused for every step; the spotlight moves by
//    CSS transition between targets rather than being rebuilt.
//
// 3. Target emphasis uses the Web Animations API on the individual
//    `scale` property. That composes with, and never cancels, the panels'
//    own transform / box-shadow animations, and leaves no inline style
//    behind.
//
// 4. Fail-safe: all four targets must exist and be visible before the
//    tour starts. If any is missing, nothing is created and the page is
//    left untouched. Any error mid-tour tears everything down.
//
// 5. Always skippable: SKIP, Escape, a click anywhere, or "?" again.
//
// Public interface:
//     window.startResultsTour()   -> starts the tour (ignored if running)
//     window.skipResultsTour()    -> tears it down immediately
//
// =====================================================================

(function () {
    "use strict";

    // ---------------------------------------------------------------
    // CONFIGURATION
    //   300ms pause + 4 x 1700ms steps + 320ms fade = ~7.4s total.
    // ---------------------------------------------------------------

    var START_DELAY = 300;   // brief pause after "?" before step 1
    var STEP_HOLD = 1700;    // time on each target, including the glide
    var GLIDE = 450;         // must match the spotlight transition in CSS
    var FADE_OUT = 320;      // must match the root opacity transition
    var PAD = 8;             // spotlight padding around each target

    // The only four targets. Each already exists in result_page.html.
    var STEPS = [
        {
            selector: ".final-score",
            title: "YOUR FINAL SCORE",
            body: "Your team's final score for the completed mission."
        },
        {
            selector: ".mission-achievement",
            title: "MISSION ACHIEVEMENT",
            body: "Your team's performance is reflected in this achievement."
        },
        {
            selector: "#challenge-results",
            title: "MISSION RESULTS",
            body: "Review what happened during each challenge."
        },
        {
            selector: ".result-inventory",
            title: "ITEM INVENTORY",
            body: "Review the items your team had available during the mission."
        }
    ];


    // ---------------------------------------------------------------
    // STATE
    // ---------------------------------------------------------------

    var running = false;
    var timers = [];
    var targets = [];
    var root = null;
    var spotlight = null;
    var card = null;
    var cardTitle = null;
    var cardBody = null;
    var cardStep = null;
    var currentTarget = null;
    var emphasis = null;
    var lastFocused = null;
    var repositionQueued = false;


    function reducedMotion() {
        return (
            window.matchMedia &&
            window.matchMedia("(prefers-reduced-motion: reduce)").matches
        );
    }

    function later(fn, delay) {
        timers.push(window.setTimeout(function () {
            if (!running) return;
            try {
                fn();
            } catch (err) {
                endTour();
            }
        }, delay));
    }

    function isVisible(el) {
        var rect = el.getBoundingClientRect();
        return rect.width > 0 && rect.height > 0;
    }


    // ---------------------------------------------------------------
    // FAIL-SAFE
    // Every target must be present and laid out, or the tour does not run.
    // ---------------------------------------------------------------

    function findTargets() {
        var found = [];

        for (var i = 0; i < STEPS.length; i++) {
            var el = document.querySelector(STEPS[i].selector);
            if (!el || !isVisible(el)) return null;
            found.push(el);
        }

        return found;
    }


    // ---------------------------------------------------------------
    // OVERLAY — built once, reused for every step
    // ---------------------------------------------------------------

    function buildOverlay() {
        root = document.createElement("div");
        root.className = "results-tour";

        // The scrim catches clicks so the page cannot be used mid-tour;
        // any click on it skips. The darkening itself is the spotlight's
        // outer shadow, which is what lets the lit area glide.
        var scrim = document.createElement("div");
        scrim.className = "results-tour-scrim";
        scrim.addEventListener("click", endTour);

        spotlight = document.createElement("div");
        spotlight.className = "results-tour-spotlight";
        spotlight.setAttribute("aria-hidden", "true");

        card = document.createElement("div");
        card.className = "results-tour-card";
        card.setAttribute("role", "dialog");
        card.setAttribute("aria-label", "Results tour");

        cardStep = document.createElement("p");
        cardStep.className = "results-tour-step";

        cardTitle = document.createElement("h2");

        cardBody = document.createElement("p");
        cardBody.setAttribute("aria-live", "polite");

        var skip = document.createElement("button");
        skip.type = "button";
        skip.className = "results-tour-skip";
        skip.textContent = "SKIP";
        skip.setAttribute("aria-label", "Skip the results tour");
        skip.addEventListener("click", function (event) {
            event.stopPropagation();
            endTour();
        });

        card.append(cardStep, cardTitle, cardBody, skip);
        root.append(scrim, spotlight, card);
        document.body.appendChild(root);

        document.addEventListener("keydown", onKeyDown);
        window.addEventListener("resize", queueReposition);
        if (window.visualViewport) {
            window.visualViewport.addEventListener("resize", queueReposition);
        }

        return skip;
    }

    function onKeyDown(event) {
        if (event.key === "Escape") endTour();
    }


    // ---------------------------------------------------------------
    // POSITIONING
    // Measured from getBoundingClientRect(), which already includes the
    // scale applied by screen_layout.js, so it works at any viewport.
    // ---------------------------------------------------------------

    function litRect(target) {
        var r = target.getBoundingClientRect();
        return {
            left: r.left - PAD,
            top: r.top - PAD,
            width: r.width + PAD * 2,
            height: r.height + PAD * 2,
            right: r.right + PAD,
            bottom: r.bottom + PAD
        };
    }

    function positionSpotlight(lit) {
        root.style.setProperty("--spotlight-x", lit.left + "px");
        root.style.setProperty("--spotlight-y", lit.top + "px");
        root.style.setProperty("--spotlight-width", lit.width + "px");
        root.style.setProperty("--spotlight-height", lit.height + "px");
    }

    function overlapArea(a, b) {
        var w = Math.min(a.right, b.right) - Math.max(a.left, b.left);
        var h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
        return w > 0 && h > 0 ? w * h : 0;
    }

    function clamp(value, min, max) {
        return Math.max(min, Math.min(max, value));
    }

    // Tries below, above, right, then left of the lit area. The first
    // placement that fits on screen without covering the target wins;
    // failing that, the one that covers the least of it.
    function positionCard(lit) {
        var vw = document.documentElement.clientWidth;
        var vh = document.documentElement.clientHeight;
        var cw = card.offsetWidth;
        var ch = card.offsetHeight;
        var gap = 14;
        var margin = 10;

        var centreX = lit.left + lit.width / 2 - cw / 2;
        var centreY = lit.top + lit.height / 2 - ch / 2;

        var options = [
            { side: "below", x: centreX, y: lit.bottom + gap },
            { side: "above", x: centreX, y: lit.top - ch - gap },
            { side: "right", x: lit.right + gap, y: centreY },
            { side: "left",  x: lit.left - cw - gap, y: centreY }
        ];

        var best = null;

        for (var i = 0; i < options.length; i++) {
            var o = options[i];

            // Keep the card on screen, then check it clears the target.
            o.x = clamp(o.x, margin, Math.max(margin, vw - cw - margin));
            o.y = clamp(o.y, margin, Math.max(margin, vh - ch - margin));
            o.cover = overlapArea(
                { left: o.x, top: o.y, right: o.x + cw, bottom: o.y + ch },
                lit
            );

            if (o.cover === 0) {
                best = o;
                break;
            }

            if (!best || o.cover < best.cover) best = o;
        }

        // Aim the pointer at the target's centre, kept on the card edge.
        var pointer = best.side === "below" || best.side === "above"
            ? clamp(lit.left + lit.width / 2 - best.x, 18, cw - 18)
            : clamp(lit.top + lit.height / 2 - best.y, 18, ch - 18);

        card.dataset.placement = best.side;
        card.style.setProperty("--pointer", (pointer - 9) + "px");
        root.style.setProperty("--card-x", best.x + "px");
        root.style.setProperty("--card-y", best.y + "px");
    }

    function reposition() {
        repositionQueued = false;
        if (!running || !currentTarget || !root) return;

        var lit = litRect(currentTarget);
        positionSpotlight(lit);
        positionCard(lit);
    }

    // screen_layout.js refits the page on the next frame after a resize,
    // so measure one frame after that.
    function queueReposition() {
        if (repositionQueued) return;
        repositionQueued = true;
        window.requestAnimationFrame(function () {
            window.requestAnimationFrame(reposition);
        });
    }


    // ---------------------------------------------------------------
    // EMPHASIS
    // One-time lift of the target via the `scale` property, sized so the
    // grown panel never spills past the spotlight's padding.
    // ---------------------------------------------------------------

    function emphasise(target) {
        if (reducedMotion() || typeof target.animate !== "function") return;

        var rect = target.getBoundingClientRect();
        var longest = Math.max(rect.width, rect.height, 1);
        var peak = 1 + Math.min(0.04, (PAD * 1.2) / longest);

        try {
            emphasis = target.animate(
                [
                    { scale: "1" },
                    { scale: String(peak), offset: 0.45 },
                    { scale: "1" }
                ],
                { duration: 600, delay: GLIDE * 0.6, easing: "ease-out" }
            );
        } catch (err) {
            emphasis = null; // `scale` unsupported: the glow alone still shows
        }
    }

    function cancelEmphasis() {
        if (emphasis) {
            try { emphasis.cancel(); } catch (err) { /* already gone */ }
            emphasis = null;
        }
    }


    // ---------------------------------------------------------------
    // STEPS
    // ---------------------------------------------------------------

    function showStep(index) {
        var step = STEPS[index];
        var target = targets[index];

        // A target removed mid-tour: stop rather than spotlight nothing.
        if (!target.isConnected || !isVisible(target)) {
            endTour();
            return;
        }

        cancelEmphasis();
        currentTarget = target;

        cardStep.textContent = (index + 1) + " / " + STEPS.length;
        cardTitle.textContent = step.title;
        cardBody.textContent = step.body;

        var lit = litRect(target);
        positionSpotlight(lit);
        positionCard(lit);

        // Restart the one-shot arrival glow on the ring and the card.
        if (!reducedMotion()) {
            spotlight.classList.remove("is-arriving");
            card.classList.remove("is-arriving");
            void spotlight.offsetWidth;
            spotlight.classList.add("is-arriving");
            card.classList.add("is-arriving");
        }

        emphasise(target);

        later(function () {
            if (index + 1 < STEPS.length) {
                showStep(index + 1);
            } else {
                endTour();
            }
        }, STEP_HOLD);
    }


    // ---------------------------------------------------------------
    // TEARDOWN — safe to call at any time, any number of times
    // ---------------------------------------------------------------

    function endTour() {
        if (!running) return;
        running = false;

        timers.forEach(window.clearTimeout);
        timers = [];
        cancelEmphasis();

        document.removeEventListener("keydown", onKeyDown);
        window.removeEventListener("resize", queueReposition);
        if (window.visualViewport) {
            window.visualViewport.removeEventListener("resize", queueReposition);
        }

        var doomed = root;
        root = spotlight = card = cardTitle = cardBody = cardStep = null;
        currentTarget = null;
        targets = [];

        if (doomed) {
            doomed.dataset.visible = "false";
            doomed.style.pointerEvents = "none";

            window.setTimeout(function () {
                if (doomed.parentNode) doomed.parentNode.removeChild(doomed);
            }, reducedMotion() ? 0 : FADE_OUT);
        }

        if (lastFocused && typeof lastFocused.focus === "function") {
            try { lastFocused.focus({ preventScroll: true }); } catch (err) { /* ignore */ }
        }
        lastFocused = null;
    }


    // ---------------------------------------------------------------
    // PUBLIC ENTRY POINT
    // ---------------------------------------------------------------

    function startResultsTour() {
        if (running) return;

        try {
            var found = findTargets();
            if (!found) return; // fail-safe: page left exactly as it is

            running = true;
            targets = found;
            lastFocused = document.activeElement;

            // Measure step 1 before the overlay exists and set it in the
            // same frame, so the spotlight appears in place rather than
            // gliding in from its default position.
            currentTarget = targets[0];
            var firstLit = litRect(currentTarget);
            var skip = buildOverlay();
            positionSpotlight(firstLit);

            window.requestAnimationFrame(function () {
                if (!running) return;
                root.dataset.visible = "true";
                try { skip.focus({ preventScroll: true }); } catch (err) { /* ignore */ }
            });

            later(function () { showStep(0); }, START_DELAY);
        } catch (err) {
            // Presentation must never break the results page.
            endTour();
        }
    }

    window.startResultsTour = startResultsTour;
    window.skipResultsTour = endTour;


    // ---------------------------------------------------------------
    // WIRING — the "?" button toggles the tour
    // ---------------------------------------------------------------

    document.addEventListener("DOMContentLoaded", function () {
        var trigger = document.getElementById("resultsTourBtn");
        if (!trigger) return;

        trigger.addEventListener("click", function () {
            if (running) {
                endTour();
            } else {
                startResultsTour();
            }
        });
    });
})();
