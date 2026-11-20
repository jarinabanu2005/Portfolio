
const menuIcon = document.getElementById("menuIcon");
const navLinks = document.getElementById("navLinks");

// Mobile navigation menu
menuIcon.addEventListener("click", function () {
    navLinks.classList.toggle("active");
});

// Close menu after clicking navigation links
document.querySelectorAll(".nav-links a").forEach(function (link) {
    link.addEventListener("click", function () {
        navLinks.classList.remove("active");
    });
});

// Automatically update footer year
document.getElementById("year").textContent =
    new Date().getFullYear();
