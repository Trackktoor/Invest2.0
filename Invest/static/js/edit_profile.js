
function displaySelectedPhoto(event) {
    var input = event.target;
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function(e) {
        document.getElementsByClassName('avatar_img')[0].src = e.target.result;
      }
      reader.readAsDataURL(input.files[0]);
    }
}

function addPhotoInProfile(event) {
  event.preventDefault()
  const photos_container = document.getElementsByClassName('profile_photos')[0]
  let imageInput = document.getElementById('profile_photos-input')

  let itemTempalte = document.getElementById('template_profile_photo')
  let item_clone = document.importNode(itemTempalte.content, true)
  let item_container = item_clone.children[0]
  // let dustbin_a = item_clone.children[1]
  // console.log(item_clone)
  // item_container.appendChild(dustbin_a)

  item_container.style.backgroundImage = 'url(' + URL.createObjectURL(imageInput.files[0]) + ')'
  item_container.name = imageInput.value.split('\\')[2]
  let label_input_photos = document.getElementsByClassName('profile_photos')[0].getElementsByTagName('label')[0]
  item_container.getElementsByClassName('delete_image__icon')[0].addEventListener('click', delete_photo_profile)
  photos_container.insertBefore(item_container, label_input_photos)
  profile_photos.push(imageInput.files[0])
}

function delete_photo_profile(ev){
  ev = ev.target.parentNode.parentNode

  let photos_a = document.getElementsByClassName('profile_photos')[0].getElementsByClassName('photo_item_a')
  for (let i = 0; i < photos_a.length; i++){
    ev.remove()
    }
  for(let i = 0; i < profile_photos.length; i++){
    console.log(profile_photos[i].name)

    img_url = ev.style['background-image']
    const regex = /url\(['"]?(.*?)['"]?\)/;
    const match = img_url.match(regex);
    const url = match ? match[1] : null;
    url_split = url.split('/')
    file_name = url_split[url_split.length-1]
    console.log(file_name)
    if (profile_photos[i].name == file_name || profile_photos[i].name == ev.name){
      profile_photos.splice(i,1)
      return
    }
  }
}

document.getElementById('profile_photos-input').addEventListener('change', addPhotoInProfile)
document.getElementById('avatar').addEventListener('change', displaySelectedPhoto)

photo_items_a__delete_images = document.getElementsByClassName('delete_image__icon')


for (let i = 0; i < photo_items_a__delete_images.length; i++){
  photo_items_a__delete_images[i].addEventListener('click', delete_photo_profile)
}

document.getElementById('form_submit').addEventListener('click', function(e){
  e.preventDefault()

  let form = new FormData()

  let avatar = document.getElementById('avatar').files[0]
  let username = document.getElementById('username').value
  let status = document.getElementById('status').value
  let profile_info = document.getElementById('profile_info_input').value

  let csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value

  form.append('avatar', avatar)
  form.append('username', username)
  form.append('status', status)
  form.append('profile_info', profile_info)

  for (let i=0; i < profile_photos.length; i++) {
    form.append('images', profile_photos[i])
  }

  var xhr = new XMLHttpRequest();

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
  console.log(form)
  xhr.send(form);
})