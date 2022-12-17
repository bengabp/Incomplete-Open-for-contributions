// let pageNavigationButtons = document.querySelectorAll("button.pg-nav");

// pageNavigationButtons.forEach(pgBtn => {
//     pgBtn.addEventListener("click",navigatePage);
    
// })

// function navigatePage(event){
//     let target = event.target;
//     let pglink = target.attributes["data-pgnav"];
//     window.location = pglink.value;
// }

$(document).ready(()=>{
    console.log("document ready");    
});


function scrollToSec(id){
    document.getElementById(id).scrollIntoView({behavior:"smooth"});
    console.log("Scrolling to ",id)
}