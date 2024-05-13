'use strict'

const themeSwitcher = document.getElementById('themeBtn')

themeSwitcher.addEventListener('click', function(){
    document.body.classList.toggle('light-theme') 
    let classes = document.body.classList; 
    var isDarkTheme = classes.contains("light-theme");
});





