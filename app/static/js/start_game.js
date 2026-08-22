const startAuctionBtn = document.getElementById("startAuctionBtn");

const helpBtn = document.getElementById("helpBtn");
const helpPopup = document.getElementById("helpPopup");
const closeHelpBtn = document.getElementById("closeHelpBtn");


function showHelp() {
    helpPopup.classList.remove("hidden");

    requestAnimationFrame(() => {
        helpPopup.classList.add("show");
    });
}


function hideHelp() {
    helpPopup.classList.remove("show");

    setTimeout(() => {
        helpPopup.classList.add("hidden");
    }, 200);
}


helpBtn.addEventListener("click", showHelp);

closeHelpBtn.addEventListener("click", hideHelp);


helpPopup.addEventListener("click", (event) => {

    if (event.target === helpPopup) {
        hideHelp();
    }

});


startAuctionBtn.addEventListener("click", () => {
    window.location.href = "/auction";
});