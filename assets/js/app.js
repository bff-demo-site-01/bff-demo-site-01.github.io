// Common shared application logic for loading header/footer partials

async function loadComponents() {
    try {
        const [headerResponse, footerResponse] = await Promise.all([
            fetch('layout/header.html'),
            fetch('layout/footer.html')
        ]);

        if (!headerResponse.ok || !footerResponse.ok) {
            throw new Error('Failed to load shared components.');
        }

        const [headerHtml, footerHtml] = await Promise.all([
            headerResponse.text(),
            footerResponse.text()
        ]);

        const headerPlaceholder = document.getElementById('header-placeholder');
        const footerPlaceholder = document.getElementById('footer-placeholder');

        if (headerPlaceholder) {
            headerPlaceholder.innerHTML = headerHtml;
            executeScripts(headerPlaceholder);
        }

        if (footerPlaceholder) {
            footerPlaceholder.innerHTML = footerHtml;
            executeScripts(footerPlaceholder);
        }

        setActiveNavigation();
    } catch (error) {
        console.error('Error loading shared components:', error);
    }
}

function executeScripts(container) {
    container.querySelectorAll('script').forEach(oldScript => {
        const newScript = document.createElement('script');
        Array.from(oldScript.attributes).forEach(attr => {
            newScript.setAttribute(attr.name, attr.value);
        });

        newScript.textContent = oldScript.textContent;
        oldScript.parentNode.removeChild(oldScript);
        document.body.appendChild(newScript);
    });
}

function setActiveNavigation() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const productPages = [
        'our-products.html',
        'sofa.html',
        'mate.html',
        'screen.html',
        'flower.html',
        'bouquet.html',
        'mums.html',
        'carnation.html'
    ];

    const navLinks = document.querySelectorAll('.nav-link-desktop');
    navLinks.forEach(link => {
        link.classList.remove('active');
        const href = link.getAttribute('href');
        if (!href) {
            return;
        }

        if ((href.includes('index.html') || href === '/') && (currentPage === 'index.html' || currentPage === '')) {
            link.classList.add('active');
            return;
        }

        if (href.includes('our-products.html') && productPages.includes(currentPage)) {
            link.classList.add('active');
            return;
        }

        if (href.includes('#services') && currentPage === 'index.html') {
            link.classList.add('active');
        }
    });
}
