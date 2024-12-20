const togglePasswordVisibility = (event) => {

    const input = event.target.previousElementSibling;
    const type = input.getAttribute('type') === 'password' ? 'text' : 'password'
    if (type == 'password') {
        event.target.setAttribute('src', '/static/img/no_eye.svg')
        event.target.setAttribute('style', 'top: calc(50% - 14px);')
    } else {
        event.target.setAttribute('src', '/static/img/eye.svg')
        event.target.setAttribute('style', 'top: calc(50% - 9px);')
    }
    input.setAttribute('type', type)
};

document.querySelectorAll('.personal-password-container').forEach(img => {
    img.addEventListener('click', togglePasswordVisibility);
});