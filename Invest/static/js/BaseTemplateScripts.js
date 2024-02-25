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

    if (burger_menu.classList.contains('active')){
        burger_menu.classList.remove('active')
        burger_menu.style.position = ''
        overlay.style.display = 'none'
        overlay.style.backgroundColor = "rgba(0, 0, 0, 0)";
        burger_menu_sub_menu.style.right = '-999px'
    } else {
        burger_menu.style.position = 'fixed'
        burger_menu.style.right = '10%'
        burger_menu_sub_menu.style.right = '0px'
        burger_menu.classList.add('active')
        overlay.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
        overlay.style.display = "block";
    }
}