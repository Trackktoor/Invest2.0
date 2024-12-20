function simulate_press_alt(e) {
    let event = new KeyboardEvent('keydown', {
        key: 'Alt', // Нажата клавиша Alt
        altKey: true, // Устанавливаем, что нажата именно клавиша Alt
    });
    e.target.dispatchEvent(event);
}

function foo(e) {
    setTimeout(function () {
        // Игнорируем нажатия клавиш, которые не являются цифрами или Backspace
        if (!/\d/.test(e.key) && e.key !== 'Backspace') {
            return;
        }

        let input = e.target.value.replace(/\D/g, ''); // Удаляем все нецифровые символы

        // Если вводим первую цифру, добавляем +7
        if (input.length === 1 && e.key !== 'Backspace') {
            input = '7' + e.key; // Добавляем 7 перед первой цифрой
        } 
        let x = input.match(/(\d{1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
        if (x) {
            e.target.value = '+7 ' + (x[2] ? '(' + x[2] : '') + (x[3] ? ') ' + x[3] : '') + (x[4] ? '-' + x[4] : '') + (x[5] ? '-' + x[5] : '');
        }

        // Обработка Backspace
        if (e.key === 'Backspace') {
            if (input.length > 0) {
                let x = input.match(/(\d{1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
                console.log(x)
                if (x) {
                    e.target.value = '+7 ' + (x[2] ? '(' + x[2] : '') + (x[3] ? ') ' + x[3] : '') + (x[4] ? '-' + x[4] : '') + (x[5] ? '-' + x[5] : '');
                }
            }
        }
    }, 0);
}

function toggleTooltip() {
    const tooltip = document.getElementById('tooltip');
    tooltip.style.display = tooltip.style.display === 'none' ? 'block' : 'none';
}

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

document.getElementById('avatar-input').addEventListener('change', function(event) {
    const file = event.target.files[0]; // Получаем выбранный файл
    if (file) {
        const reader = new FileReader(); // Создаем объект FileReader
        reader.onload = function(e) {
            document.getElementById('avatar-preview').src = e.target.result; // Устанавливаем src для img
        };
        reader.readAsDataURL(file); // Читаем файл как Data URL
    }
});

document.querySelectorAll('.personal-password-container').forEach(img => {
    img.addEventListener('click', togglePasswordVisibility);
});

document.querySelector('input[name="phone"]').addEventListener('keydown', foo);