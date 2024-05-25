'use strict'

const themeSwitcher = document.getElementById('themeBtn')

themeSwitcher.addEventListener('click', function(){
    document.body.classList.toggle('light-theme') 
    let classes = document.body.classList; 
    var isDarkTheme = classes.contains("light-theme");
});

document.addEventListener("DOMContentLoaded", function() {
    const textarea = document.getElementById("prompt");

    textarea.addEventListener("keydown", function(event) {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();
            // Envia o formulário ou realiza a ação desejada
            document.querySelector("button.form-input-btn").click();
        }
    });

    // Ajusta a altura do textarea automaticamente
    textarea.addEventListener("input", function() {
        this.style.height = "auto";
        this.style.height = (this.scrollHeight) + "px";
    });
});