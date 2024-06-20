let sliders_arr = [];
document.addEventListener("DOMContentLoaded", function() {
    const slidesContainer = document.getElementById('slides-container');
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    
    let currentIndex = 0;

    function updateSlider() {
        const offset = -currentIndex * 100;
        slidesContainer.style.transform = `translateX(${offset}%)`;
        console.log('slide')
    }

    if (!(window.location.pathname.startsWith("/project/"))) {
        const fileInput = document.getElementById('fileInput');
        const addSlideButton = document.getElementById('addSlide');
        const removeSlideButton = document.getElementById('removeSlide');
        var slides = [];
        function addSlide(imageSrc, file) {
            const newSlide = document.createElement('div');
            newSlide.classList.add('slide');
    
            const img = document.createElement('img');
            img.src = imageSrc;
            newSlide.appendChild(img);
    
            slidesContainer.appendChild(newSlide);
            slides.push(newSlide);
            sliders_arr.push(file);
            updateSlider();
        }
        fileInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    addSlide(e.target.result, file);
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
    }
    else {
        var slides = document.getElementsByClassName('slide');
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
        console.log('2')
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


    nextButton.addEventListener('click', function(event) {
        event.preventDefault();
        showNextSlide();
    });

    prevButton.addEventListener('click', function(event) {
        event.preventDefault();
        showPrevSlide();
    });
});
