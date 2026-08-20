document.addEventListener("DOMContentLoaded", () => {

    // Result data waiting on backend
    const gameResult = {
        finalScore: null,
        leftoverMoney: null,
        failures: null,
        missions: []
    };


    // Display final score
    function displayFinalScore(score) {
        const scoreElement = document.getElementById("final-score");

        if (scoreElement) {
            scoreElement.textContent = score ?? "---";
        }
    }


    // Display leftover money
    function displayLeftoverMoney(money) {
        const moneyElement = document.getElementById("leftover-money");

        if (moneyElement) {
            moneyElement.textContent = money !== null
                ? `$${money}`
                : "$---";
        }
    }


    // Display mission results. NEED TO KNOW: how many mission per game, how is diffculty rated, scoring logic
    function displayMissionResults(missions) {
        const missionCards = document.querySelectorAll(".mission-card");

        missions.forEach((mission, index) => {
            const card = missionCards[index];

            if (!card) return;

            const difficulty = card.querySelector(".difficulty");//here
            const score = card.querySelector(".mission-score");//here

            if (difficulty) {
                difficulty.textContent = mission.difficulty ?? "---";
            }

            if (score) {
                score.textContent = mission.score ?? "---";
            }
        });
    }


    // Initialise result page
    function loadResults() {
        displayFinalScore(gameResult.finalScore);
        displayLeftoverMoney(gameResult.leftoverMoney);
        displayMissionResults(gameResult.missions);
    }


    // Run when result page loads
    loadResults();

});