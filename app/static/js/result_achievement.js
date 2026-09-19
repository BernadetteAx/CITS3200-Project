// =====================================================================
// RESULT_ACHIEVEMENT.JS — Mission Achievement category
// =====================================================================
//
// Classifies the team's performance from the score the backend already
// sent, and renders it as an earned badge in the panel that replaced
// LEFTOVER MONEY.
//
// DESIGN NOTES FOR REVIEWERS
//
// 1. No score is calculated here. `result.finalScore` arrives exactly as
//    scoring_service.py produced it; this file only maps that number to
//    a display category. Nothing is sent back to the server.
//
// 2. Like results_tour.js, this attaches its OWN listener to the
//    existing "result_state" event rather than editing result_page.js.
//    Socket.IO supports multiple listeners, and deferred scripts run in
//    document order, so displayResults() still runs first.
//
// 3. Re-rendering is idempotent — repeated result_state events simply
//    redraw the same panel.
//
// Public interface:
//     window.getAchievement(score) -> { tier, title, emblem, description }
//
// =====================================================================

(function () {
    "use strict";

    // ---------------------------------------------------------------
    // CATEGORIES
    //
    // Bands are continuous inside 1-100 so no score falls through a
    // gap: the brief lists 1-40 / 50-70 / 80-100, which leaves 41-49
    // and 71-79 unstated. Those settle into the band below them.
    // Anything outside 1-100, or not a number at all, gets the
    // unranked fallback rather than throwing.
    // ---------------------------------------------------------------

    var ACHIEVEMENTS = {
        achieved: {
            tier: "achieved",
            title: "CHALLENGE ACHIEVEMENT",
            emblem: "emblem-challenge-achievement.png",
            description:
                "Your team achieved an outstanding performance and completed the mission with excellence."
        },
        fair: {
            tier: "fair",
            title: "FAIR CHALLENGE WIN",
            emblem: "emblem-fair-challenge-win.png",
            description:
                "Your team completed the mission with a satisfactory performance."
        },
        failed: {
            tier: "failed",
            title: "FAILED MISSION",
            emblem: "emblem-failed-mission.png",
            description:
                "The crew completed the mission, but the mission performance was poor."
        },
        unranked: {
            tier: "unranked",
            title: "UNRANKED RESULT",
            emblem: null,
            description: "This mission score could not be ranked."
        }
    };


    function getAchievement(score) {
        var value = Number(score);

        // Fallback: missing, non-numeric, or outside the ranked range.
        if (!isFinite(value) || value < 1 || value > 100) {
            return ACHIEVEMENTS.unranked;
        }

        if (value >= 80) return ACHIEVEMENTS.achieved;
        if (value >= 50) return ACHIEVEMENTS.fair;

        return ACHIEVEMENTS.failed;
    }


    // ---------------------------------------------------------------
    // RENDERING
    // ---------------------------------------------------------------

    function renderAchievement(score) {
        var panel = document.querySelector(".mission-achievement");
        var emblem = document.getElementById("achievement-emblem");
        var title = document.getElementById("achievement-title");

        // Fail-safe: not the results page, or the panel was removed.
        if (!panel || !emblem || !title) return;

        var achievement = getAchievement(score);

        title.textContent = achievement.title;

        // data-tier drives both the emblem artwork and the accent colour
        // from result_achievement.css.
        panel.dataset.tier = achievement.tier;
        emblem.dataset.tier = achievement.tier;

        // The emblem is decorative reinforcement; the category is always
        // present as text. The fuller description is exposed to assistive
        // technology on the panel itself.
        emblem.setAttribute("aria-hidden", "true");
        panel.setAttribute(
            "aria-label",
            "Mission achievement: " + achievement.title + ". " + achievement.description
        );

        // One-time reveal; re-arm only if the tier actually changed.
        if (!panel.classList.contains("is-revealed")) {
            panel.classList.add("is-revealed");
        }
    }


    window.getAchievement = getAchievement;
    window.renderAchievement = renderAchievement;


    // ---------------------------------------------------------------
    // AUTO-WIRING
    // A second listener on the existing event; result_page.js unchanged.
    // ---------------------------------------------------------------

    document.addEventListener("DOMContentLoaded", function () {
        try {
            var socket = window.gameSocket;
            if (!socket || typeof socket.on !== "function") return;

            socket.on("result_state", function (result) {
                try {
                    renderAchievement(result ? result.finalScore : null);
                } catch (err) {
                    /* presentation must never break the results page */
                }
            });
        } catch (err) {
            /* no socket: the panel simply keeps its placeholder */
        }
    });
})();
