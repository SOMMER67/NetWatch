// NetWatch - Fonctions JavaScript interactives

// Filtre de recherche sur les équipements du tableau de bord
document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("deviceSearch");
    const devicesTable = document.getElementById("devicesTable");

    if (searchInput && devicesTable) {
        searchInput.addEventListener("input", (e) => {
            const query = e.target.value.toLowerCase();
            const rows = devicesTable.querySelectorAll("tbody tr");

            rows.forEach((row) => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(query) ? "" : "none";
            });
        });
    }
});

// Simulation de rafraîchissement des temps de réponse (ping)
function refreshPings() {
    const pingBadges = document.querySelectorAll(".ping-badge");
    pingBadges.forEach((badge) => {
        const currentPing = parseInt(badge.textContent, 10);
        // Variation légère de +/- 2ms sans descendre en dessous de 1ms
        const delta = Math.floor(Math.random() * 5) - 2;
        const newPing = Math.max(1, currentPing + delta);
        badge.textContent = `${newPing} ms`;
        
        badge.style.transition = "color 0.3s ease";
        badge.style.color = "#2563EB";
        setTimeout(() => {
            badge.style.color = "var(--green-700)";
        }, 400);
    });
}
