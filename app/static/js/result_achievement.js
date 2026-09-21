// =====================================================================
// RESULT_ACHIEVEMENT.JS — Mission Achievement category
// =====================================================================
//
// Classifies the team's performance from the challenges-passed count
// the backend already sent, and renders it as an earned badge in the
// panel that replaced LEFTOVER MONEY.
//
// DESIGN NOTES FOR REVIEWERS
//
// 1. Nothing is calculated here. `result.challengesPassed` arrives exactly
//    as scoring_service.py produced it; this file only maps that count to
//    a display category. Nothing is sent back to the server.
//
// 2. Like results_crt.js, this attaches its OWN listener to the
//    existing "result_state" event rather than editing result_page.js.
//    Socket.IO supports multiple listeners, and deferred scripts run in
//    document order, so displayResults() still runs first.
//
// 3. Re-rendering is idempotent — repeated result_state events simply
//    redraw the same panel.
//
// Public interface:
//     window.getAchievement(challengesPassed) -> { tier, title, emblem, description }
//
// =====================================================================

(function () {
    "use strict";

    // ---------------------------------------------------------------
    // CATEGORIES
    //
    // Ranked on the number of challenges the crew PASSED, out of the
    // six a mission always has. Titles, artwork and copy come from
    // images/six_badges_achievements.png.
    //
    //   6 passed  -> PERFECT EXECUTION
    //   5 passed  -> SUPERIOR SUCCESS
    //   4 passed  -> FAIR CHALLENGE WIN
    //   1-3 passed-> FAILED MISSION   (the sheet states 3; 1 and 2 are
    //                                  unstated and settle here)
    //   0 passed  -> CATASTROPHIC FAILURE
    //
    // A missing or non-numeric count gets the unranked fallback rather
    // than throwing.
    // ---------------------------------------------------------------

    var ACHIEVEMENTS = {
        perfect: {
            tier: "perfect",
            title: "PERFECT EXECUTION",
            emblem: "emblem-perfect-execution.png",
            description:
                "The crew achieved flawless synchronization, completing all 6 challenges with zero errors."
        },
        superior: {
            tier: "superior",
            title: "SUPERIOR SUCCESS",
            emblem: "emblem-superior-success.png",
            description:
                "Your team displayed excellent coordination, completing 5 challenges with high proficiency."
        },
        fair: {
            tier: "fair",
            title: "FAIR CHALLENGE WIN",
            emblem: "emblem-fair-challenge-win.png",
            description:
                "Your team completed the mission with a satisfactory performance across 4 challenges."
        },
        failed: {
            tier: "failed",
            title: "FAILED MISSION",
            emblem: "emblem-failed-mission.png",
            description:
                "The crew finished the core objective, but mission performance was poor with only 3 challenges met."
        },
        catastrophic: {
            tier: "catastrophic",
            title: "CATASTROPHIC FAILURE",
            emblem: "emblem-catastrophic-failure.png",
            description:
                "Total system collapse. The crew was entirely overwhelmed, failing to clear a single challenge."
        },
        unranked: {
            tier: "unranked",
            title: "UNRANKED RESULT",
            emblem: null,
            description: "This mission result could not be ranked."
        }
    };


    function getAchievement(challengesPassed) {
        // Fallback: missing or non-numeric. Checked before Number(), which
        // would otherwise turn null into 0 and mislabel it catastrophic.
        if (challengesPassed == null || challengesPassed === "") {
            return ACHIEVEMENTS.unranked;
        }

        var passed = Number(challengesPassed);
        if (!isFinite(passed)) return ACHIEVEMENTS.unranked;

        if (passed >= 6) return ACHIEVEMENTS.perfect;
        if (passed === 5) return ACHIEVEMENTS.superior;
        if (passed === 4) return ACHIEVEMENTS.fair;
        if (passed >= 1) return ACHIEVEMENTS.failed;

        return ACHIEVEMENTS.catastrophic;
    }


    // ---------------------------------------------------------------
    // RENDERING
    // ---------------------------------------------------------------

    function renderAchievement(challengesPassed) {
        var panel = document.querySelector(".mission-achievement");
        var emblem = document.getElementById("achievement-emblem");
        var title = document.getElementById("achievement-title");

        // Fail-safe: not the results page, or the panel was removed.
        if (!panel || !emblem || !title) return;

        var achievement = getAchievement(challengesPassed);

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
                    renderAchievement(result ? result.challengesPassed : null);
                } catch (err) {
                    /* presentation must never break the results page */
                }
            });
        } catch (err) {
            /* no socket: the panel simply keeps its placeholder */
        }
    });
})();
