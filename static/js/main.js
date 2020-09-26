function navToggle(){
    const nav = document.querySelector(".main__nav");
    if(nav.style.minHeight == '75vh'){
        nav.style.minHeight = "10vh";
        var toggleIcon = document.querySelector('.toggle__icons');
        toggleIcon.innerHTML = "<i class='fa fa-bars' ></i>"
    }
    else{
        nav.style.minHeight = '75vh';
        var toggleIcon = document.querySelector('.toggle__icons');
        toggleIcon.innerHTML = "<i class='fa fa-times' ></i>";
    }
}

const toggleCollapse = document.querySelector('.toggle__collapse').addEventListener('click', navToggle);