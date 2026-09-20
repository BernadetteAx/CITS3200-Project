// =====================================================================
// RESULTS_TOUR.JS — "Results Spotlight" post-game reveal
// =====================================================================
//
// A short, one-shot spotlight tour that guides the player's attention to
// the headline areas of the results page: the FINAL SCORE panel, the
// MISSION ACHIEVEMENT badge, and the MISSION RESULTS panel.
//
// DESIGN NOTES FOR REVIEWERS
//
// 1. This file is entirely self-contained. It renders no results data of
//    its own — it only observes DOM nodes that result_page.js has
//    already filled in. Scores, challenges and items are still produced
//    exclusively by the existing code.
//
// 2. It does NOT modify result_page.js. Socket.IO allows more than one
//    listener per event, so this file attaches a SECOND listener to
//    "result_state". socket.js is a classic script at the end of <body>,
//    so it runs before the deferred page scripts; deferred scripts then
//    run in document order, which means result_page.js registers
//    displayResults first and therefore runs first. By the time the
//    listener below fires, the DOM already holds the real values.
//
// 3. Everything is fail-safe. If the socket, the panels or the score are
//    missing, the tour quietly does nothing and the results page behaves
//    exactly as it does today.
//
// Public interface:
//     window.startResultsTour()   -> starts the tour (once per page load)
//     window.skipResultsTour()    -> tears it down immediately
//
// =====================================================================

(function () {
    "use strict";

    // ---------------------------------------------------------------
    // CONFIGURATION
    // ---------------------------------------------------------------

    // Timings are deliberately unhurried: the player gets a beat to take
    // the results in before the spotlight appears, and each panel stays
    // lit long enough to actually read it.
    //   3s pause + 4s on the score + 4s on the breakdown = ~11s total.
    var START_DELAY = 500;   // pause after results land, before step 1
    var STEP_HOLD = 4000;     // how long each step stays lit
    var SCROLL_SETTLE = 380;  // allow a smooth scroll to finish

    // Each step points at an existing element. Nothing here is created
    // by this feature — these panels already exist in result_page.html.
    var STEPS = [
        {
            selector: ".final-score",
            title: "YOUR TEAM'S SCORE",
            body: "Your final score reflects the choices your crew made throughout the mission.",
            emphasise: "#final-score"
        },
        {
            selector: ".mission-achievement",
            title: "MISSION ACHIEVEMENT",
            body: "This badge is the rank your crew earned for the score they finished on.",
            emphasise: "#achievement-emblem"
        },
        {
            selector: ".mission-results",
            title: "MISSION BREAKDOWN",
            body: "Review how your team's decisions affected each challenge.",
            emphasise: null
        }
    ];


    // ---------------------------------------------------------------
    // STATE
    // ---------------------------------------------------------------

    var tourStarted = false;  // guards against repeated result_state events
    var tourFinished = false;
    var timers = [];
    var root = null;
    var spotlight = null;
    var card = null;
    var currentTarget = null;
    var lastFocused = null;


    function reducedMotion() {
        return (
            window.matchMedia &&
            window.matchMedia("(prefers-reduced-motion: reduce)").matches
        );
    }

    function later(fn, delay) {
        var id = window.setTimeout(function () {
            if (!tourFinished) fn();
        }, delay);

        timers.push(id);
        return id;
    }

    function clearTimers() {
        timers.forEach(window.clearTimeout);
        timers = [];
    }


    // ---------------------------------------------------------------
    // OVERLAY CONSTRUCTION
    // All markup is built here so result_page.html stays untouched.
    // ---------------------------------------------------------------

    function buildOverlay() {
        root = document.createElement("div");
        root.className = "results-tour";

        var scrim = document.createElement("div");
        scrim.className = "results-tour-scrim";
        // Clicking anywhere outside the coach mark skips the tour.
        scrim.addEventListener("click", endTour);

        spotlight = document.createElement("div");
        spotlight.className = "results-tour-spotlight";

        card = document.createElement("div");
        card.className = "results-tour-card";
        card.setAttribute("role", "dialog");
        card.setAttribute("aria-live", "polite");
        card.setAttribute("aria-label", "Results highlights");

        root.appendChild(scrim);
        root.appendChild(spotlight);
        root.appendChild(card);

        document.body.appendChild(root);

        document.addEventListener("keydown", onKeyDown);
        window.addEventListener("resize", reposition);
        window.addEventListener("scroll", reposition, { passive: true });
    }

    function onKeyDown(event) {
        // Escape is a conventional way out; focus is never trapped.
        if (event.key === "Escape") endTour();
    }


    // ---------------------------------------------------------------
    // POSITIONING
    // Driven entirely by getBoundingClientRect(), so the spotlight
    // tracks the real element at any viewport size or scroll offset.
    // ---------------------------------------------------------------

    function positionSpotlight(target) {
        var rect = target.getBoundingClientRect();
        var pad = 8;

        root.style.setProperty("--spotlight-x", (rect.left - pad) + "px");
        root.style.setProperty("--spotlight-y", (rect.top - pad) + "px");
        root.style.setProperty("--spotlight-width", (rect.width + pad * 2) + "px");
        root.style.setProperty("--spotlight-height", (rect.height + pad * 2) + "px");
    }

    function positionCard(target) {
        var rect = target.getBoundingClientRect();
        var cardRect = card.getBoundingClientRect();
        var vw = document.documentElement.clientWidth;
        var vh = document.documentElement.clientHeight;
        var gap = 16;
        var margin = 12;

        // Prefer sitting below the panel; flip above when there is no room.
        var placement = "below";
        var y = rect.bottom + gap;

        if (y + cardRect.height > vh - margin) {
            var above = rect.top - cardRect.height - gap;

            if (above >= margin) {
                placement = "above";
                y = above;
            } else {
                // Neither side fits (very short viewport): clamp on screen.
                y = Math.max(margin, vh - cardRect.height - margin);
            }
        }

        // Keep the card fully inside the viewport horizontally.
        var x = rect.left;
        var maxX = vw - cardRect.width - margin;

        if (x > maxX) x = maxX;
        if (x < margin) x = margin;

        // Aim the pointer at the centre of the target, but keep it on the card.
        var pointer = rect.left + rect.width / 2 - x;
        pointer = Math.max(18, Math.min(cardRect.width - 18, pointer));

        card.dataset.placement = placement;
        root.style.setProperty("--card-x", x + "px");
        root.style.setProperty("--card-y", y + "px");
        card.style.setProperty("--pointer-x", (pointer - 9) + "px");
    }

    function reposition() {
        if (tourFinished || !currentTarget || !root) return;

        positionSpotlight(currentTarget);
        positionCard(currentTarget);
    }


    // ---------------------------------------------------------------
    // SCROLLING
    // Only scrolls when the panel is genuinely out of view, so the
    // player's page is not yanked around unnecessarily.
    // ---------------------------------------------------------------

    function bringIntoView(target, done) {
        var rect = target.getBoundingClientRect();
        var vh = document.documentElement.clientHeight;
        var visible = rect.top >= 0 && rect.bottom <= vh;

        if (visible) {
            done();
            return;
        }

        try {
            target.scrollIntoView({
                behavior: reducedMotion() ? "auto" : "smooth",
                block: "center"
            });
        } catch (err) {
            target.scrollIntoView();
        }

        later(done, reducedMotion() ? 0 : SCROLL_SETTLE);
    }


    // ---------------------------------------------------------------
    // STEPS
    // ---------------------------------------------------------------

    function renderCard(step) {
        card.innerHTML = "";

        var heading = document.createElement("h2");
        heading.textContent = step.title;

        var body = document.createElement("p");
        body.textContent = step.body;

        var skip = document.createElement("button");
        skip.type = "button";
        skip.className = "results-tour-skip";
        skip.textContent = "SKIP";
        skip.setAttribute("aria-label", "Skip the results highlights");
        skip.addEventListener("click", function (event) {
            event.stopPropagation();
            endTour();
        });

        card.appendChild(heading);
        card.appendChild(body);
        card.appendChild(skip);

        // Restart the entrance animation on each step.
        if (!reducedMotion()) {
            card.style.animation = "none";
            void card.offsetWidth;
            card.style.animation = "";
        }

        return skip;
    }

    function showStep(index) {
        if (tourFinished) return;

        var step = STEPS[index];
        var target = document.querySelector(step.selector);

        // Fail-safe: skip a panel that is not on the page rather than
        // abandoning the whole tour, so removing one section does not
        // stop the remaining steps from running.
        if (!target) {
            if (index + 1 < STEPS.length) {
                showStep(index + 1);
            } else {
                endTour();
            }
            return;
        }

        currentTarget = target;

        bringIntoView(target, function () {
            if (tourFinished) return;

            var skip = renderCard(step);

            positionSpotlight(target);

            // Measure the card once it has its real content, then place it.
            window.requestAnimationFrame(function () {
                if (tourFinished) return;

                positionCard(target);
                root.dataset.visible = "true";

                // Keyboard users land on SKIP; focus is not trapped and the
                // page is not scrolled by the focus call itself.
                if (index === 0 && skip) {
                    try {
                        skip.focus({ preventScroll: true });
                    } catch (err) {
                        /* older browsers: focus options unsupported */
                    }
                }
            });

            // One controlled pop on the score — transform only.
            if (step.emphasise && !reducedMotion()) {
                var scoreEl = document.querySelector(step.emphasise);

                if (scoreEl) {
                    scoreEl.classList.add("results-tour-pop");
                    later(function () {
                        scoreEl.classList.remove("results-tour-pop");
                    }, 700);
                }
            }

            // Advance, or finish. The tour never loops.
            later(function () {
                if (index + 1 < STEPS.length) {
                    showStep(index + 1);
                } else {
                    endTour();
                }
            }, STEP_HOLD);
        });
    }


    // ---------------------------------------------------------------
    // TEARDOWN
    // Safe to call at any time, any number of times.
    // ---------------------------------------------------------------

    function endTour() {
        if (tourFinished) return;

        tourFinished = true;
        clearTimers();

        document.removeEventListener("keydown", onKeyDown);
        window.removeEventListener("resize", reposition);
        window.removeEventListener("scroll", reposition);

        var pop = document.querySelector(".results-tour-pop");
        if (pop) pop.classList.remove("results-tour-pop");

        if (!root) return;

        root.dataset.visible = "false";
        root.style.pointerEvents = "none";

        var doomed = root;

        var remove = function () {
            if (doomed && doomed.parentNode) doomed.parentNode.removeChild(doomed);
        };

        root = null;
        spotlight = null;
        card = null;
        currentTarget = null;

        if (reducedMotion()) {
            remove();
        } else {
            window.setTimeout(remove, 320);
        }

        if (lastFocused && typeof lastFocused.focus === "function") {
            try {
                lastFocused.focus({ preventScroll: true });
            } catch (err) {
                /* ignore */
            }
        }
    }


    // ---------------------------------------------------------------
    // PUBLIC ENTRY POINT
    // ---------------------------------------------------------------

    function startResultsTour() {
        // Runs once per page load, no matter how often result_state arrives.
        if (tourStarted) return;

        try {
            var score = document.getElementById("final-score");
            var scorePanel = document.querySelector(".final-score");
            var missionPanel = document.querySelector(".mission-results");

            // Fail-safe: not the results page, or results not populated yet.
            if (!score || !scorePanel || !missionPanel) return;

            var value = (score.textContent || "").trim();
            if (value === "" || value === "---") return;

            tourStarted = true;
            lastFocused = document.activeElement;

            buildOverlay();
            later(function () { showStep(0); }, START_DELAY);
        } catch (err) {
            // Presentation must never break the results page.
            tourStarted = true;
            endTour();
        }
    }

    window.startResultsTour = startResultsTour;
    window.skipResultsTour = endTour;


    // ---------------------------------------------------------------
    // AUTO-WIRING
    // A second listener on the existing event. result_page.js is not
    // touched, and its own handler still runs first.
    // ---------------------------------------------------------------

    document.addEventListener("DOMContentLoaded", function () {
        try {
            var socket = window.gameSocket;
            if (!socket || typeof socket.on !== "function") return;

            socket.on("result_state", function () {
                // Wait one frame so the existing render has finished.
                window.requestAnimationFrame(function () {
                    window.requestAnimationFrame(startResultsTour);
                });
            });
        } catch (err) {
            /* no socket: the results page simply shows no tour */
        }
    });
})();
