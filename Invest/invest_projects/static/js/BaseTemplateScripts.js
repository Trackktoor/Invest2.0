const burger_menu = document.getElementsByClassName('burger_menu')[0]
const overlay = document.getElementsByClassName('overlay')[0]

burger_menu.addEventListener('click', BurgerMenuFunction)
overlay.addEventListener('click', OverlayHidden)


function OverlayHidden(){
    let overlay = document.getElementsByClassName('overlay')[0]
    overlay.style.display = 'none'
    burger_menu.style.position = ''
    BurgerMenuFunction()
}   

function BurgerMenuFunction(){
    let burger_menu = document.getElementsByClassName('burger_menu')[0]
    let overlay = document.getElementsByClassName('overlay')[0]
    let burger_menu_sub_menu = document.getElementsByClassName('burger_menu_sub_menu')[0]
    let left_header_logo = document.getElementsByClassName('left_header_logo')[0]
    console.log(left_header_logo)
    try {
        if (left_header_logo.classList.contains('burger_menu_logo')) {
            left_header_logo.classList.remove('burger_menu_logo')
        }
        else {
            left_header_logo.classList.add('burger_menu_logo')
        }
    }catch {

    }


    if (burger_menu.classList.contains('active')){
        burger_menu.classList.remove('active')
        burger_menu.style.position = ''
        overlay.style.display = 'none'
        overlay.style.backgroundColor = "rgba(0, 0, 0, 0)";
        burger_menu_sub_menu.style.left = '-999px'
    } else {
        burger_menu.style.position = 'fixed'
        burger_menu.style.left = '5%'
        if (window.innerWidth <= 1100){
            burger_menu.style.left = '17%'
        }
        if (window.innerWidth <= 800){
            burger_menu.style.left = '16%'
        }
        if (window.innerWidth <= 496){
            burger_menu.style.left = '24%'
            burger_menu_sub_menu.style.left = '20%'
    }
        burger_menu_sub_menu.style.left = '0'

        burger_menu.classList.add('active')
        overlay.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
        overlay.style.display = "block";
    }
}