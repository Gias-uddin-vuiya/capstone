document.addEventListener("DOMContentLoaded", () => {
    let expandIcon = document.querySelector(".expand-icon");
    let contractIcon = document.querySelector(".contract-icon");
    let detailImage = document.getElementById("detail-image");


    
    contractIcon.style.display = "none";
    expandIcon.addEventListener("click", () => {
        expandIcon.style.display = "none";
        contractIcon.style.display = "block";
        
        document.documentElement.requestFullscreen();
    });

    contractIcon.addEventListener("click", () => {  
        contractIcon.style.display = "none";
        expandIcon.style.display = "block";
        document.exitFullscreen();  
    });

});

