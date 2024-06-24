document.addEventListener('DOMContentLoaded', () => {
    const langLinks = document.querySelectorAll('[data-lang]');
    langLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const lang = e.target.getAttribute('data-lang');
            window.location.href = `/${lang}/`;
        });
    });
});