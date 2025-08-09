document.addEventListener('DOMContentLoaded', () => {
    const langLinks = document.querySelectorAll('[data-lang]');
    langLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const lang = e.target.getAttribute('data-lang');
            window.location.href = `/${lang}/`;
        });
    });

    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.querySelector('.main-nav');
    const body = document.body;

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', function() {
            const isActive = this.classList.contains('active');
            
            this.classList.toggle('active');
            mainNav.classList.toggle('active');
            body.classList.toggle('menu-open');
            
            if (!isActive) {
                body.style.overflow = 'hidden';
            } else {
                body.style.overflow = '';
            }
        });

        const navLinks = document.querySelectorAll('.main-nav a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                mainNav.classList.remove('active');
                body.classList.remove('menu-open');
                body.style.overflow = '';
            });
        });

        document.addEventListener('click', (e) => {
            if (!mainNav.contains(e.target) && !menuToggle.contains(e.target)) {
                menuToggle.classList.remove('active');
                mainNav.classList.remove('active');
                body.classList.remove('menu-open');
                body.style.overflow = '';
            }
        });
    }

    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const headerHeight = document.getElementById('sticky-header').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    const catalogItems = document.querySelectorAll('.catalog-item, .section-item, .letter-item');
    catalogItems.forEach((item, index) => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(20px)';
        item.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        observer.observe(item);
    });

    initializeFilters();
    initializeSearch();
});

function initializeFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn, .filter-tag');
    const catalogItems = document.querySelectorAll('.catalog-item');
    
    if (filterButtons.length === 0) return;

    let activeFilters = new Set();

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filter = this.dataset.filter || this.textContent.replace('★', '').trim();
            
            if (this.classList.contains('active')) {
                this.classList.remove('active');
                activeFilters.delete(filter);
            } else {
                this.classList.add('active');
                activeFilters.add(filter);
            }

            applyFilters(activeFilters, catalogItems);
            updateURL(activeFilters);
        });
    });

    loadFiltersFromURL(activeFilters, filterButtons, catalogItems);
}

function initializeSearch() {
    const searchInput = document.getElementById('catalog-search') || document.getElementById('search-input');
    if (!searchInput) return;

    let searchTimeout;
    
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
            const searchTerm = this.value.toLowerCase().trim();
            const catalogItems = document.querySelectorAll('.catalog-item');
            
            catalogItems.forEach(item => {
                const title = item.querySelector('h2').textContent.toLowerCase();
                const description = item.querySelector('p').textContent.toLowerCase();
                const isVisible = !searchTerm || title.includes(searchTerm) || description.includes(searchTerm);
                
                item.style.display = isVisible ? 'block' : 'none';
            });
            
            updateResultsCount();
        }, 300);
    });
}

function applyFilters(activeFilters, catalogItems) {
    catalogItems.forEach(item => {
        if (activeFilters.size === 0) {
            item.style.display = 'block';
            return;
        }

        const itemFilters = Array.from(item.querySelectorAll('.filter-tag'))
            .map(tag => tag.textContent.toLowerCase().replace('★', '').trim());
        
        const matchesFilter = Array.from(activeFilters).every(filter =>
            itemFilters.some(itemFilter => itemFilter.includes(filter.toLowerCase()))
        );

        item.style.display = matchesFilter ? 'block' : 'none';
    });
    
    updateResultsCount();
}

function updateResultsCount() {
    const visibleItems = document.querySelectorAll('.catalog-item[style*="display: block"], .catalog-item:not([style*="display: none"])');
    const totalItems = document.querySelectorAll('.catalog-item').length;
    
    console.log(`Showing ${visibleItems.length} of ${totalItems} items`);
}

function updateURL(activeFilters) {
    const url = new URL(window.location);
    
    if (activeFilters.size > 0) {
        url.searchParams.set('filters', Array.from(activeFilters).join(','));
    } else {
        url.searchParams.delete('filters');
    }
    
    history.replaceState(null, '', url);
}

function loadFiltersFromURL(activeFilters, filterButtons, catalogItems) {
    const url = new URL(window.location);
    const urlFilters = url.searchParams.get('filters');
    
    if (urlFilters) {
        const filters = urlFilters.split(',');
        
        filters.forEach(filter => {
            activeFilters.add(filter);
            
            const button = Array.from(filterButtons).find(btn => {
                const btnFilter = btn.dataset.filter || btn.textContent.replace('★', '').trim();
                return btnFilter.toLowerCase() === filter.toLowerCase();
            });
            
            if (button) {
                button.classList.add('active');
            }
        });
        
        applyFilters(activeFilters, catalogItems);
    }
}