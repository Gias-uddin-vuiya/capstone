document.addEventListener("DOMContentLoaded", () => {
  const expandIcon = document.querySelector(".expand-icon");
  const contractIcon = document.querySelector(".contract-icon");
  const imageContainer = document.querySelector(".image-view");

  if (!expandIcon || !contractIcon || !imageContainer) return;

  // Initial state
  contractIcon.style.display = "none";

  // Enter fullscreen
  expandIcon.addEventListener("click", () => {
    if (imageContainer.requestFullscreen) {
      imageContainer.requestFullscreen();
    } else if (imageContainer.webkitRequestFullscreen) {
      imageContainer.webkitRequestFullscreen();
    } else if (imageContainer.msRequestFullscreen) {
      imageContainer.msRequestFullscreen();
    }
  });

  // Exit fullscreen
  contractIcon.addEventListener("click", () => {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    } else if (document.webkitExitFullscreen) {
      document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) {
      document.msExitFullscreen();
    }
  });

  // Handle ESC key / gesture exit
  document.addEventListener("fullscreenchange", () => {
    const isFullscreen = document.fullscreenElement !== null;

    expandIcon.style.display = isFullscreen ? "none" : "block";
    contractIcon.style.display = isFullscreen ? "block" : "none";
  });
});
