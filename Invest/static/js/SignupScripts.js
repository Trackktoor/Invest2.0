// input_file = document.getElementsByClassName('file_input')[0]
// input_file.addEventListener('change',check_input_file)


// function check_input_file(){
//     console.log('11')
//     input_text = document.getElementsByClassName('photo_help_text')[0]
//     if(this.value){
//         file_name_split = this.value.split('\\')
//         file_name = file_name_split[file_name_split.length-1]
//         input_text.innerHTML = file_name.slice(0,10) + '...'
//     }
//     else{
//         input_text.innerHTML = 'Обзор'
//     }
// }

// document.getElementsByName('phone')[0].addEventListener('input', function (e) {
//     console.log(e)
//     // console.log(e.target.value)
//     if (e.key != 'Backspace') {
//         console.log("KEY")
//         console.log('Key pressed:', e.key);
//         console.log('Key code:', e.keyCode);
//         console.log('Ctrl key pressed:', e.ctrlKey);
//         console.log('Shift key pressed:', e.shiftKey);
//         console.log('Alt key pressed:', e.altKey);
//         console.log('Meta key pressed:', e.metaKey);
//         let input = e.target.value.replace(/\D/g, '');
//         if (input.length == 1) {
//             input = '7'+input
//         }
//         console.log(input)
//         console.log('dwwwa')
//         let x = input.match(/(\d{1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
//         if (x) {
//             e.target.value = '+7 ' + (x[2] ? '(' + x[2] : '') + (x[3] ? ') ' + x[3] : '') + (x[4] ? '-' + x[4] : '') + (x[5] ? '-' + x[5] : '');
//         }
//     }
// });
// document.getElementsByName('phone')[0].addEventListener('keydown', function (e) { 
//     if (e.key === 'Backspace') {
//       let value = e.target.value.replace(/\D/g, ''); // удаляем все нецифровые символы
//       console.log('До удаления: ' + value)
//       value = value.slice(0, -1); // удаляем последнюю цифру
//       console.log('После удаления: ' + value)
//     //   console.log('STR')
//     //   console.log(value)
//       if (value.length > 0) {
//         if (e.target.value.length == 1) {
//             e.target.value = ''
//         }
//         else{
//             e.target.value = '+7 (' + value.substring(0, 3) + ') ' + value.substring(3, 6) + '-' + value.substring(6, 8) + '-' + value.substring(8, 10);
//         }
//       }
//       e.target.value = value;
//     }
//   }
// )

function simulate_press_alt(e) {
    let event = new KeyboardEvent('keydown', {
        key: 'Alt', // Нажата клавиша Alt
        altKey: true, // Устанавливаем, что нажата именно клавиша Alt
    });
    e.target.dispatchEvent(event);
}

function foo(e) {
    setTimeout(function (){
        if (e.key != 'Backspace') {
        
            // console.log("KEY")
            console.log('Key pressed:', e.key);
            // console.log('e.target.value = ', this.value);
            if (e.target.value == ''){
                e.target.value = e.key
            }
            

            
            let input = e.target.value.replace(/\D/g, '');
            // if (e.target.value == ''){
            //     input = e.key
            // }
            // if (input.length == 1) {
            //     input = '7'+input
            // }
            console.log(input)
    
            let x = input.match(/(\d{1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
            console.log(x)
            if (x) {
                e.target.value = '+7 ' + (x[2] ? '(' + x[2] : '') + (x[3] ? ') ' + x[3] : '') + (x[4] ? '-' + x[4] : '') + (x[5] ? '-' + x[5] : '');
            }
        }
        if (e.key === 'Backspace') {
            let value = e.target.value.replace(/\D/g, ''); // удаляем все нецифровые символы
            //   console.log('STR')
            //   console.log(value)
            if (value.length > 0) {
                if (e.target.value.length == 1) {
                    e.target.value = ''
                }
                else{
                    let x = value.match(/(\d{1})(\d{0,3})(\d{0,3})(\d{0,2})(\d{0,2})/);
                    console.log(x)
                    if (x) {
                        e.target.value = '+7 ' + (x[2] ? '(' + x[2] : '') + (x[3] ? ') ' + x[3] : '') + (x[4] ? '-' + x[4] : '') + (x[5] ? '-' + x[5] : '');
                    }
                }
            }
        }
    
    }, 0)


}

document.getElementsByName('phone')[0].addEventListener('keydown', foo);
