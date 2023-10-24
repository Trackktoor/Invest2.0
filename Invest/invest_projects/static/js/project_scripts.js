// Получаем элементы слайдера
const slider = document.querySelector('.slider');
const prevButton = document.querySelector('.back');
const nextButton = document.querySelector('.next');
const slides = Array.from(slider.querySelectorAll('img'));
const slideCount = slides.length;
const slides_length = slides.length
let slideIndex = 0;


nextButton.addEventListener('click', function() {
    if (slideIndex < slides_length-1){
        slideIndex++
    }
    else{
        slideIndex = 0
    }

    slide()
})

prevButton.addEventListener('click', function() {
    if (slideIndex != 0){
        slideIndex--
    }
    else {
        slideIndex = 0
    }
    slide()

})

function slide(){
    console.log(slideIndex)
    
    slider.style.transform = `translateX(-${slider.offsetWidth * slideIndex}px)`;
}