document.addEventListener('DOMContentLoaded', function() {
    // Handle image fallbacks
    document.querySelectorAll('img').forEach(img => {
        img.onerror = function() {
            const iconDiv = this.nextElementSibling;
            if (iconDiv) {
                this.style.display = 'none';
                iconDiv.style.display = 'inline-block';
            }
        };
    });

    // Animation observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate__animated', entry.target.dataset.animation);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('[data-animation]').forEach((el) => observer.observe(el));
});
