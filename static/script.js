document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".genre-card");
    if (cards.length < 3) return;

    const positions = ["card-front", "card-back-right", "card-back-left"];
    let index = 0;

    setInterval(() => {
        cards.forEach(card =>
            card.classList.remove(...positions)
        );

        cards.forEach((card, i) => {
            card.classList.add(positions[(i + index) % 3]);
        });

        index = (index + 1) % 3;
    }, 3000);
});




    const toggle = document.getElementById("theme-toggle");
    const root = document.documentElement;

    // Load saved theme
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        root.setAttribute("data-theme", savedTheme);
        toggle.textContent = savedTheme === "dark" ? "☀️" : "🌙";
    }

    toggle.addEventListener("click", () => {
        const isDark = root.getAttribute("data-theme") === "dark";
        const newTheme = isDark ? "light" : "dark";

        root.setAttribute("data-theme", newTheme);
        localStorage.setItem("theme", newTheme);
        toggle.textContent = newTheme === "dark" ? "☀️" : "🌙";
    });