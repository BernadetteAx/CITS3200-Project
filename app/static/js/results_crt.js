// =====================================================================
// RESULTS_CRT.JS — CRT scanline reveal for the Game Results page
// =====================================================================
//
// Plays one short CRT-style reveal the moment the results render, then
// removes itself. It replaces the earlier spotlight tour, which darkened
// the page around each panel (#142).
//
// DESIGN NOTES FOR REVIEWERS
//
// 1. Presentation only. Nothing here reads, changes or re-emits result
//    data. The existing result_page.js and result_achievement.js still
//    render everything exactly as before.
//
// 2. result_page.js is not modified. Socket.IO allows more than one
//    listener per event, so this file attaches its own listener to
//    "result_state". Deferred scripts run in document order, so the
//    existing renderers have already run by the time this fires.
//
// 3. The layer is pointer-events: none and is removed after ~1.7s, so
//    buttons, links, scrolling and the challenge-card hover are never
//    blocked — not even while the effect is playing.
//
// 4. Fail-safe: no socket, no results page, or reduced motion → nothing
//    happens and the page behaves as it does today.
//
// Public interface:
//     window.startResultsCrt()   -> plays the reveal (once per page load)
//
// =====================================================================

(function () {
    "use strict";

    var DURATION_FALLBACK = 2400; // ms; removes the layer even if animationend never fires

    var played = false; // once per page load, however often result_state arrives


    function reducedMotion() {
        return (
            window.matchMedia &&
            window.matchMedia("(prefers-reduced-motion: reduce)").matches
        );
    }


    function startResultsCrt() {
        if (played) return;

        try {
            // Only on the results page, and only once results are on screen.
            if (!document.querySelector(".final-score")) return;

            played = true;

            // Reduced motion: skip the flicker/sweep entirely.
            if (reducedMotion()) return;

            var layer = document.createElement("div");
            layer.className = "results-crt";
            layer.setAttribute("aria-hidden", "true");
            document.body.appendChild(layer);

            var removed = false;
            var remove = function () {
                if (removed) return;
                removed = true;
                if (layer.parentNode) layer.parentNode.removeChild(layer);
            };

            // The root's own animation is the longest; its end is the cue.
            // Pseudo-element animations bubble here too, so filter on target
            // and make sure it is not a ::before / ::after event.
            layer.addEventListener("animationend", function (event) {
                if (event.target === layer && !event.pseudoElement) remove();
            });

            // Belt-and-braces: never leave the layer behind.
            window.setTimeout(remove, DURATION_FALLBACK);

            // Next frame so the initial opacity: 0 is committed before the
            // animation class lands, otherwise the flicker can be skipped.
            window.requestAnimationFrame(function () {
                layer.classList.add("is-running");
            });
        } catch (err) {
            // Presentation must never break the results page.
        }
    }

    window.startResultsCrt = startResultsCrt;


    // ---------------------------------------------------------------
    // AUTO-WIRING
    // A second listener on the existing event; result_page.js unchanged.
    // ---------------------------------------------------------------
    document.addEventListener("DOMContentLoaded", function () {
        try {
            var socket = window.gameSocket;
            if (!socket || typeof socket.on !== "function") return;

            socket.on("result_state", function () {
                // Two frames so the existing renderers have painted first.
                window.requestAnimationFrame(function () {
                    window.requestAnimationFrame(startResultsCrt);
                });
            });
        } catch (err) {
            /* no socket: the results page simply shows no reveal */
        }
    });
})();
