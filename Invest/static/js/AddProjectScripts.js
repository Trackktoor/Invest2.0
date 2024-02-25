document.getElementById('avatar-input').addEventListener('change', previewAvatar)
document.getElementById('header_background-input').addEventListener('change', previewHeaderBackground)
document.getElementById('slider_photos-input').addEventListener('change', addSlide)
document.getElementById('delete_slide').addEventListener('click', deleteSlide)

/* Зависимости для слайдера */
// Получаем элементы слайдера
const slider = document.querySelector('.slider');
const prevButton = document.querySelector('.back');
const nextButton = document.querySelector('.next');
const imageInput = document.getElementById('slider_photos-input')

let form = document.getElementsByClassName('project_container')[0]

let sliders_arr = []

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

function addSlide(event) {
  event.preventDefault()
  const slider = document.getElementsByClassName('slider')[0]

  if (imageInput.files.length > 0) {
    const slide_img = document.createElement('img')
    slide_img.src = URL.createObjectURL(imageInput.files[0])
    slide_img.classList.add('slider_img_item')
    slide_img.name = imageInput.files[0].name
    slider.appendChild(slide_img)
    sliders_arr.push(imageInput.files[0])
  }
}

function deleteSlide() {
  img_name = slider.querySelectorAll('img')[slideIndex].name

  for (let i=0; i < sliders_arr.length; i++){
    if (sliders_arr[i].name == img_name) {
      sliders_arr.splice(i,1)
    }
  }

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

let project_main_info =  document.getElementsByClassName('project_main_info')[0]

document.querySelector('#project_description_textarea').style.width = (project_main_info.offsetWidth-30) + 'px'

function getTextWidth(text) {
  var canvas = document.createElement("canvas");
  var context = canvas.getContext("2d");
  context.font = window.getComputedStyle(document.getElementById("project_city")).getPropertyValue("font");
  var metrics = context.measureText(text);
  return metrics.width;
}

document.getElementById('project_city').addEventListener('input', function(e){
  textWidth = getTextWidth(e.target.value)
  if (+textWidth >= 100){
    e.target.style.width = textWidth+'px'
  }
  else {
    e.target.style.width = '100px'
  }
})

document.getElementById('form_submit').addEventListener('click', function(e){
  e.preventDefault()

  let form = new FormData()

  let avatar = document.getElementById('avatar-input')
  let title = document.getElementById('title-input').value
  let profit = document.getElementById('profit-input').value
  let profit_parametrs = document.getElementsByName('profit_parametr')
  let background_image = document.getElementsByName('background-image')[0]
  let profit_parametr = ''
  for (let i=0; i < profit_parametrs.length; i++){
    if (profit_parametrs[i].checked){
      profit_parametr = profit_parametrs[i].value
    }
  }

  let required_invest = document.getElementById('required_invest').value  
  let author_job_title = document.getElementById('author_job_title').value
  let author_phone_number = document.getElementById('author_phone_number').value
  let project_description = document.getElementById('project_description_textarea').value
  let project_city = document.getElementById('project_city').id

  let csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
  let category = document.getElementsByName('category')[0].value

  form.append('project_avatar', avatar.files[0])
  form.append('title', title)
  form.append('profit_per_month', profit)
  form.append('profit_parametr', profit_parametr)
  form.append('author_job_title', author_job_title)
  form.append('contacts', author_phone_number)
  form.append('description', project_description)
  form.append('city', project_city)
  form.append('category', category)

  for (let i=0; i < sliders_arr.length; i++) {
    form.append('images', sliders_arr[i])
  }
  form.append('background_image', background_image.files[0])

  form.append('required_investment', required_invest)
  
  var xhr = new XMLHttpRequest();

  console.log(window.location.href)
  xhr.open("POST", window.location.href, true);
  xhr.setRequestHeader("X-CSRFToken", csrfmiddlewaretoken);

  xhr.onload = function() {
    console.log(xhr)
    if (xhr.status === 200) {
      console.log(xhr)
      console.log("Ответ с сервера:", xhr.responseText);
      window.location.href = JSON.parse(xhr.responseText)['reverse_url'];
    } else {
      console.log("Произошла ошибка:", xhr.status);
    }
  };

  xhr.send(form);
})