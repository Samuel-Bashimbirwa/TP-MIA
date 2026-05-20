// JS Enhancements for TP MIA Web Portal
document.addEventListener("DOMContentLoaded", () => {
    console.log("TP MIA portal initialized in MVC mode!");

    // Highlight the active menu item in the sidebar
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll(".nav-item a");
    
    let matched = false;
    navLinks.forEach(link => {
        const href = link.getAttribute("href");
        if (currentPath === href) {
            link.parentElement.classList.add("active");
            matched = true;
        } else {
            link.parentElement.classList.remove("active");
        }
    });

    // If no path matches exactly (e.g. sub-routes), default to home or check startsWith
    if (!matched) {
        navLinks.forEach(link => {
            const href = link.getAttribute("href");
            if (href !== "/" && currentPath.startsWith(href)) {
                link.parentElement.classList.add("active");
            }
        });
    }

    // Add subtle visual effect to interactive cards
    const cards = document.querySelectorAll(".glass-panel, .stat-card, .premium-list-item");
    cards.forEach(card => {
        card.addEventListener("mousemove", (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            // Set dynamic CSS properties for spotlight cursor effect
            card.style.setProperty("--mouse-x", `${x}px`);
            card.style.setProperty("--mouse-y", `${y}px`);
        });
    });

    // Handle form loading states
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", () => {
            const submitBtn = form.querySelector("input[type='submit'], button[type='submit']");
            if (submitBtn) {
                submitBtn.value = "Saving to Database...";
                submitBtn.style.opacity = "0.7";
                submitBtn.style.cursor = "not-allowed";
            }
        });
    });
});
