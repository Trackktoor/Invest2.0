document.getElementById('avatar-input').addEventListener('change', previewAvatar)
document.getElementById('header_background-input').addEventListener('change', previewHeaderBackground)
document.getElementById('slider_photos-input').addEventListener('change', addSlide)
document.getElementById('delete_slide').addEventListener('click', deleteSlide)

/* Зависимости для слайдера */
// Получаем элементы слайдера
const slider = document.querySelector('.slider');
const prevButton = document.querySelector('.back');
const nextButton = document.querySelector('.next');

let slideIndex = 0;

function previewAvatar(event) {
    var input = event.target;
    var reader = new FileReader();
  
    reader.onload = function() {
      var image = document.getElementById("avatar-image");
      image.src = reader.result;
      image.style.display = "block";
    };
    
    reader.readAsDataURL(input.files[0]);

    let avatar_label = document.getElementsByClassName('avatar-label')[0]
    avatar_label.style.display = 'none'
}

function previewHeaderBackground(event) {
  const file = event.target.files[0];
  const reader = new FileReader();
  console.log('11')
  reader.onload = function(event) {
    var background_image = document.getElementsByClassName("project_header")[0];
    background_image.style.backgroundImage = `url(${event.target.result})`;
  };
  reader.readAsDataURL(file);
  
}

function addSlide() {
  const imageInput = document.getElementById('slider_photos-input')
  const slider = document.getElementsByClassName('slider')[0]

  if (imageInput.files.length > 0) {
    const slide_img = document.createElement('img')
    slide_img.src = URL.createObjectURL(imageInput.files[0])
    slide_img.classList.add('slider_img_item')
    slider.appendChild(slide_img)
  }
}

function deleteSlide() {
  slider.querySelectorAll('img')[slideIndex].remove()
  slideIndex = 0
  slide()
}

/* Логика слайдера */
nextButton.addEventListener('click', function() {
  let slides = Array.from(slider.querySelectorAll('img'));
  let slides_length = slides.length
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
  slider.style.transform = `translateX(-${slider.offsetWidth * slideIndex}px)`;
}

console.log(slider.offsetWidth)
console.log(slider)

let project_main_info =  document.getElementsByClassName('project_main_info')[0]

console.log()

document.getElementsByClassName('project_description')[0].style.width = (project_main_info.offsetWidth-30) + 'px'