const backgrounds = [
    'url(background1.jpg)',
    'url(background2.jpg)',
    'url(background3.jpg)'
];

let currentIndex = 0;

function changeBackground() {
    document.body.style.backgroundImage = backgrounds[currentIndex];
    currentIndex = (currentIndex + 1) % backgrounds.length;
}

setInterval(changeBackground, 5000); // Change background every 5 seconds
changeBackground(); // Initial background change
