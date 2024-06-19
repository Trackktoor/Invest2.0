let sliders_arr = [];
document.addEventListener("DOMContentLoaded", function() {
    const slidesContainer = document.getElementById('slides-container');
    const fileInput = document.getElementById('fileInput');
    const addSlideButton = document.getElementById('addSlide');
    const removeSlideButton = document.getElementById('removeSlide');
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');

    let slides = [];

    let currentIndex = 0;

    function updateSlider() {
        const offset = -currentIndex * 100;
        slidesContainer.style.transform = `translateX(${offset}%)`;
    }

    function addSlide(imageSrc) {
        const newSlide = document.createElement('div');
        newSlide.classList.add('slide');

        const img = document.createElement('img');
        img.src = imageSrc;
        newSlide.appendChild(img);

        slidesContainer.appendChild(newSlide);
        slides.push(newSlide);
        sliders_arr.push(imageSrc);
        updateSlider();
    }

    function removeSlide() {
        if (slides.length > 0) {
            const slideToRemove = slides.pop();
            slidesContainer.removeChild(slideToRemove);
            sliders_arr.pop();
            if (currentIndex >= slides.length) {
                currentIndex = slides.length - 1;
            }
            updateSlider();
        }
    }

    function showNextSlide() {
        if (currentIndex < slides.length - 1) {
            currentIndex++;
            updateSlider();
        }
    }

    function showPrevSlide() {
        if (currentIndex > 0) {
            currentIndex--;
            updateSlider();
        }
    }

    fileInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                addSlide(e.target.result);
            };
            reader.readAsDataURL(file);
        }
    });

    addSlideButton.addEventListener('click', function(event) {
        event.preventDefault();
        fileInput.click();
    });

    removeSlideButton.addEventListener('click', function(event) {
        event.preventDefault();
        removeSlide();
    });

    nextButton.addEventListener('click', function(event) {
        event.preventDefault();
        showNextSlide();
    });

    prevButton.addEventListener('click', function(event) {
        event.preventDefault();
        showPrevSlide();
    });
});
