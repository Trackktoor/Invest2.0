
document.getElementsByClassName('nav_delet_project')[0].addEventListener('click', function(e){
    let form = new FormData()
  
    var xhr = new XMLHttpRequest();
    xhr.open("POST", e.target.getAttribute('style'), true);
    let csrfmiddlewaretoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
    xhr.setRequestHeader("X-CSRFToken", csrfmiddlewaretoken);
  
    xhr.onload = function() {
      console.log(xhr)
      if (xhr.status === 200) {
        console.log(xhr)
        console.log("Ответ с сервера:", xhr.responseText);
      } else {
        console.log("Произошла ошибка:", xhr.status);
      }
    };
    xhr.send(form);

    e.target.parentNode.parentNode.remove()
})