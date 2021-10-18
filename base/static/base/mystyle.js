// Sidebar to navbar (Responsive)
let btn = document.querySelector("#collapse-btn");
let navbar = document.querySelector(".mobile-nav");
let content = document.querySelector(".content");

btn.onclick = function() {
    navbar.classList.toggle("active");
    content.classList.toggle("active");
}

// Date for today tab
let today = new Date();
let date = today.getFullYear()+'/'+(today.getMonth()+1)+'/'+today.getDate();
document.querySelector(".today-date").innerHTML = date;