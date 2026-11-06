/**
 * MSR Tent Mart - Central Application Logic & Catalogue Engine
 * Data-driven catalogue rendering, enquiry builder, base-aware path handling, and partials.
 */

// ==========================================
// 1. CONFIGURATION & STATE
// ==========================================
const SITE_CONFIG = {
    BUSINESS_NAME: 'MSR Tent Mart',
    WHATSAPP_NUMBER: '916384500051',
    WHATSAPP_DISPLAY: '+91 63845 00051',
    BUSINESS_EMAIL: '', // If empty, email line is completely hidden
    SOCIAL: {
        linkedin: '',
        instagram: 'https://www.instagram.com/msr.tentmart.decorations',
        facebook: '',
        youtube: '',
        other: ''
    }
};

const CATALOGUE_CONFIG = {
    whatsappNumber: SITE_CONFIG.WHATSAPP_NUMBER,
    whatsappCandidateNumbers: ['+91 63845 00051'],
    whatsappStatus: 'CONFIRMED',
    whatsappEnabled: true,
    currencySymbol: '₹',
    missingPriceLabel: 'Price on Request',
    catalogueJsonPath: 'assets/json/product_list.json'
};

let _catalogueCache = null;

// ==========================================
// 2. PATH & URL RESOLUTION
// ==========================================
function getBasePath() {
    const path = window.location.pathname;
    const isSubfolder = path.includes('/categories/') || 
                        path.includes('/products/') || 
                        path.includes('/about/') || 
                        path.includes('/contact/') || 
                        path.includes('/privacy/') || 
                        path.includes('/terms/');
    return isSubfolder ? '../' : './';
}

function resolveAssetPath(relPath) {
    if (!relPath) return '';
    if (relPath.startsWith('http://') || relPath.startsWith('https://') || relPath.startsWith('//') || relPath.startsWith('data:')) {
        return relPath;
    }
    const clean = relPath.replace(/^(\.\/|\/)/, '');
    return getBasePath() + clean;
}

function escapeHtml(str) {
    if (str === null || str === undefined) return '';
    return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}

// ==========================================
// 3. CATALOGUE DATA ACCESS
// ==========================================
async function fetchCatalogueData() {
    if (_catalogueCache) return _catalogueCache;
    const jsonUrl = resolveAssetPath(CATALOGUE_CONFIG.catalogueJsonPath);
    try {
        const response = await fetch(jsonUrl);
        if (!response.ok) {
            throw new Error(`HTTP error ${response.status} fetching catalogue`);
        }
        _catalogueCache = await response.json();
        return _catalogueCache;
    } catch (error) {
        console.error('Failed to load catalogue data:', error);
        throw error;
    }
}

// ==========================================
// 4. SHARED ENQUIRY BUILDER & MODAL
// ==========================================
function buildEnquiryMessage(product, category) {
    const categoryName = category ? category.name : (product.categoryId || 'General');
    const pageUrl = window.location.href.split('#')[0] + '#' + encodeURIComponent(product.id || product.code);
    return `Hello MSR Tent Mart,\n\nI would like to inquire about this product from your catalogue:\n\n• Product Name: ${product.name}\n• Product Code: ${product.code}\n• Category: ${categoryName}\n• Catalogue Link: ${pageUrl}\n\nPlease share price, availability, and rental details. Thank you!`;
}

async function handleProductEnquiry(productCode) {
    try {
        const data = await fetchCatalogueData();
        const product = data.products.find(p => p.code === productCode || p.id === productCode);
        if (!product) {
            console.error('Product not found for enquiry:', productCode);
            return;
        }
        const category = data.categories.find(c => c.id === product.categoryId);
        const message = buildEnquiryMessage(product, category);

        if (CATALOGUE_CONFIG.whatsappEnabled && CATALOGUE_CONFIG.whatsappNumber) {
            const cleanNumber = String(CATALOGUE_CONFIG.whatsappNumber).replace(/\D/g, '');
            const waNumber = (cleanNumber.length === 10) ? ('91' + cleanNumber) : cleanNumber;
            const encoded = encodeURIComponent(message);
            const waUrl = `https://wa.me/${waNumber}?text=${encoded}`;
            const win = window.open(waUrl, '_blank', 'noopener,noreferrer');
            if (!win || win.closed || typeof win.closed === 'undefined') {
                window.location.href = waUrl;
            }
        } else {
            // Fallback notice modal
            showEnquiryNoticeModal(product, message);
        }
    } catch (e) {
        console.error('Error handling product enquiry:', e);
    }
}

// Global alias for compatibility with old onclick calls
window.redirectToWhatsApp = function(productName, productCode) {
    handleProductEnquiry(productCode);
};

function showEnquiryNoticeModal(product, message) {
    let modalBackdrop = document.getElementById('enquiry-notice-modal');
    if (!modalBackdrop) {
        modalBackdrop = document.createElement('div');
        modalBackdrop.id = 'enquiry-notice-modal';
        modalBackdrop.className = 'enquiry-modal-backdrop';
        document.body.appendChild(modalBackdrop);
    }

    modalBackdrop.innerHTML = `
        <div class="enquiry-modal-card" role="dialog" aria-modal="true" aria-labelledby="enquiry-modal-title">
            <button class="enquiry-modal-close" aria-label="Close modal" onclick="closeEnquiryModal()">&times;</button>
            <div class="text-center mb-3">
                <i class="fab fa-whatsapp text-success fs-1 mb-2"></i>
                <h3 id="enquiry-modal-title" class="fs-4 fw-bold">Product Enquiry</h3>
                <span class="badge bg-secondary">${escapeHtml(product.code)}</span>
            </div>
            
            <div class="alert alert-info py-2 px-3 small mb-3" role="alert">
                <i class="fas fa-info-circle me-1"></i>
                Online enquiry is temporarily unavailable. Please check back soon.
            </div>

            <p class="small text-muted mb-2">Your prefilled enquiry message for <strong>${escapeHtml(product.name)}</strong>:</p>
            <div class="enquiry-message-preview" id="enquiry-preview-text">${escapeHtml(message)}</div>

            <div class="enquiry-modal-actions">
                <button type="button" class="btn btn-sm btn-outline-secondary" onclick="closeEnquiryModal()">Close</button>
                <button type="button" class="btn btn-sm btn-primary" onclick="copyEnquiryMessage()">
                    <i class="fas fa-copy me-1"></i> Copy Enquiry Message
                </button>
            </div>
            <div id="enquiry-copy-alert" class="small text-success mt-2 text-center" style="display:none;">
                <i class="fas fa-check-circle me-1"></i> Message copied to clipboard!
            </div>
        </div>
    `;

    modalBackdrop.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

function closeEnquiryModal() {
    const modalBackdrop = document.getElementById('enquiry-notice-modal');
    if (modalBackdrop) {
        modalBackdrop.style.display = 'none';
    }
    document.body.style.overflow = '';
}

function copyEnquiryMessage() {
    const preview = document.getElementById('enquiry-preview-text');
    if (!preview) return;
    navigator.clipboard.writeText(preview.textContent).then(() => {
        const alert = document.getElementById('enquiry-copy-alert');
        if (alert) {
            alert.style.display = 'block';
            setTimeout(() => { alert.style.display = 'none'; }, 3000);
        }
    }).catch(err => {
        console.error('Clipboard copy failed:', err);
    });
}

function handleProductImageError(imgEl, code) {
    imgEl.onerror = null;
    const parent = imgEl.closest('.product-img-wrap');
    if (parent) {
        parent.innerHTML = `
            <div class="product-placeholder-wrap">
                <i class="fas fa-image"></i>
                <span>Photo on Request<br><small class="text-muted">${escapeHtml(code)}</small></span>
            </div>
        `;
    }
}

// ==========================================
// 5. PRODUCT CARD RENDERING
// ==========================================
function renderProductCard(product, category) {
    const categoryName = category ? category.name : '';
    const hasImage = Boolean(product.image);
    const isGroup = Boolean(product.isGroupPhoto);
    const resolvedImg = hasImage ? resolveAssetPath(product.image) : (product.groupImage ? resolveAssetPath(product.groupImage) : '');

    let imgBlock = '';
    if (hasImage) {
        imgBlock = `
            <img src="${escapeHtml(resolvedImg)}" 
                 alt="${escapeHtml(product.altText || product.name)}" 
                 loading="lazy" 
                 onerror="handleProductImageError(this, '${escapeHtml(product.code)}')" />
        `;
    } else if (isGroup && resolvedImg) {
        imgBlock = `
            <img src="${escapeHtml(resolvedImg)}" 
                 alt="${escapeHtml(product.altText || product.name)}" 
                 loading="lazy" 
                 style="opacity: 0.9;"
                 onerror="handleProductImageError(this, '${escapeHtml(product.code)}')" />
            <span class="product-group-badge" title="Referenced in collection swatch poster">Group Swatch</span>
        `;
    } else {
        imgBlock = `
            <div class="product-placeholder-wrap">
                <i class="fas fa-palette"></i>
                <span>Color Variant<br><small class="text-muted">${escapeHtml(product.code)}</small></span>
            </div>
        `;
    }

    let priceHtml = '';
    if (product.price !== null && product.price !== undefined && product.price > 0) {
        priceHtml = `<span class="price-tag">${CATALOGUE_CONFIG.currencySymbol}${product.price}</span>`;
    } else {
        priceHtml = `<span class="price-tag enquiry-only">${CATALOGUE_CONFIG.missingPriceLabel}</span>`;
    }

    return `
        <div class="col-12 col-sm-6 col-lg-4 col-xl-3 mb-4" id="${escapeHtml(product.id)}">
            <div class="product-card">
                <div class="product-img-wrap">
                    <span class="product-code-badge">${escapeHtml(product.code)}</span>
                    ${imgBlock}
                </div>
                <div class="product-card-body">
                    <div class="product-category-tag">${escapeHtml(categoryName)}</div>
                    <h4 class="product-card-title">${escapeHtml(product.name)}</h4>
                    <p class="product-card-desc mb-2">
                        ${isGroup ? '<small class="text-muted"><i class="fas fa-info-circle me-1"></i>Part of ' + escapeHtml(categoryName) + ' color series</small>' : '<small class="text-muted">Premium event decor material</small>'}
                    </p>
                    <div class="product-meta-row">
                        ${priceHtml}
                        <button type="button" class="btn-enquire" onclick="handleProductEnquiry('${escapeHtml(product.code)}')">
                            <i class="fab fa-whatsapp"></i> Inquire
                        </button>
                    </div>
                </div>
            </div>
        </div>
    `;
}

// ==========================================
// 6. CATEGORY PAGE INITIALIZATION
// ==========================================
async function initCategoryPage(categoryId) {
    try {
        const data = await fetchCatalogueData();
        const category = data.categories.find(c => c.id.toLowerCase() === categoryId.toLowerCase());
        if (!category) {
            console.error('Unknown category ID:', categoryId);
            return;
        }

        const categoryProducts = data.products.filter(p => p.categoryId.toLowerCase() === categoryId.toLowerCase());

        // Update page meta / hero if present
        document.title = `${category.name} Collection - MSR Tent Mart`;

        const heroTitle = document.querySelector('.hero-title');
        if (heroTitle) {
            heroTitle.innerHTML = `${escapeHtml(category.name)} <span class="accent">Collection</span>`;
        }

        const heroDesc = document.querySelector('.hero-description');
        if (heroDesc) {
            heroDesc.textContent = category.description;
        }

        const heroSec = document.querySelector('.hero-section');
        if (heroSec && category.heroImage) {
            heroSec.style.backgroundImage = `url('${resolveAssetPath(category.heroImage)}')`;
        }

        const secTitle = document.querySelector('.section-title');
        if (secTitle) {
            secTitle.textContent = `${category.name} Collection (${categoryProducts.length} Items)`;
        }

        const secLabel = document.querySelector('.section-label');
        if (secLabel) {
            secLabel.innerHTML = `<i class="${category.icon} me-2"></i>${escapeHtml(category.name)} Collection`;
        }

        // Render product grid
        const grid = document.getElementById('products-grid');
        if (grid) {
            let noticeHtml = '';
            if (category.hasGroupReferenceOnly) {
                noticeHtml = `
                    <div class="col-12 mb-4">
                        <div class="alert alert-info py-3 px-4 d-flex align-items-center justify-content-between flex-wrap gap-2" role="alert">
                            <div>
                                <i class="fas fa-palette me-2 fs-5"></i>
                                <strong>${escapeHtml(category.name)} Color Swatch Collection:</strong>
                                All ${categoryProducts.length} color variants are available with verified individual codes. Source photography presents these shades together on the collection reference poster.
                            </div>
                            ${category.groupImage ? `<a href="${resolveAssetPath(category.groupImage)}" target="_blank" rel="noopener" class="btn btn-sm btn-outline-primary"><i class="fas fa-eye me-1"></i>View Full Swatch Poster</a>` : ''}
                        </div>
                    </div>
                `;
            }

            grid.innerHTML = noticeHtml + categoryProducts.map(p => renderProductCard(p, category)).join('');
        }
    } catch (err) {
        console.error('Failed to init category page:', err);
        const grid = document.getElementById('products-grid');
        if (grid) {
            grid.innerHTML = `
                <div class="col-12 text-center py-5">
                    <div class="alert alert-danger" role="alert">
                        <i class="fas fa-exclamation-triangle me-2"></i>
                        Unable to load catalogue items at this time. Please check your connection.
                    </div>
                </div>
            `;
        }
    }
}

// ==========================================
// 7. ALL-PRODUCTS PAGE INITIALIZATION
// ==========================================
async function initAllProductsPage() {
    try {
        const data = await fetchCatalogueData();
        const container = document.getElementById('products-container');
        if (!container) return;

        // Render toolbar (search + filter pills)
        let activeCategoryId = 'all';
        let searchQuery = '';

        function renderToolbar() {
            const pillsHtml = [
                `<a class="filter-pill ${activeCategoryId === 'all' ? 'active' : ''}" data-cat="all">
                    All Products <span class="pill-count">${data.products.length}</span>
                </a>`
            ].concat(data.categories.map(c => `
                <a class="filter-pill ${activeCategoryId === c.id ? 'active' : ''}" data-cat="${escapeHtml(c.id)}">
                    <i class="${c.icon} me-1"></i>${escapeHtml(c.name)} <span class="pill-count">${c.productCount}</span>
                </a>
            `)).join('');

            return `
                <div class="container-max mx-auto px-responsive pt-4">
                    <div class="catalogue-toolbar">
                        <div class="search-box-wrapper">
                            <i class="fas fa-search"></i>
                            <input type="text" id="catalogue-search" class="catalogue-search-input" 
                                   placeholder="Search by product name, code (e.g. MS_W1_001)..." 
                                   value="${escapeHtml(searchQuery)}" />
                        </div>
                        <div class="category-filter-pills" id="filter-pills-wrap">
                            ${pillsHtml}
                        </div>
                    </div>
                    <div class="results-count-bar text-center" id="results-count"></div>
                    <div class="row gap-responsive" id="all-products-grid"></div>
                </div>
            `;
        }

        container.innerHTML = renderToolbar();

        function filterAndRender() {
            const grid = document.getElementById('all-products-grid');
            const countBar = document.getElementById('results-count');
            const q = searchQuery.trim().toLowerCase();

            let filtered = data.products.filter(p => {
                const matchesCat = (activeCategoryId === 'all') || (p.categoryId.toLowerCase() === activeCategoryId.toLowerCase());
                if (!matchesCat) return false;
                if (!q) return true;
                return p.name.toLowerCase().includes(q) || 
                       p.code.toLowerCase().includes(q) || 
                       p.categoryId.toLowerCase().includes(q);
            });

            if (countBar) {
                const catName = activeCategoryId === 'all' ? 'All Products' : (data.categories.find(c => c.id === activeCategoryId)?.name || '');
                countBar.innerHTML = `Showing <strong>${filtered.length}</strong> of ${data.products.length} products ${activeCategoryId !== 'all' ? `in <em>${escapeHtml(catName)}</em>` : ''}`;
            }

            if (grid) {
                if (filtered.length === 0) {
                    grid.innerHTML = `
                        <div class="col-12 text-center py-5">
                            <div class="text-muted">
                                <i class="fas fa-box-open fs-1 mb-3 d-block text-secondary"></i>
                                <h5>No matching products found</h5>
                                <p class="small">Try adjusting your search terms or clearing category filters.</p>
                                <button type="button" class="btn btn-sm btn-outline-primary mt-2" onclick="clearFilters()">Reset Filters</button>
                            </div>
                        </div>
                    `;
                } else {
                    grid.innerHTML = filtered.map(p => {
                        const cat = data.categories.find(c => c.id === p.categoryId);
                        return renderProductCard(p, cat);
                    }).join('');
                }
            }
        }

        // Event listeners
        const searchInput = document.getElementById('catalogue-search');
        if (searchInput) {
            searchInput.addEventListener('input', (e) => {
                searchQuery = e.target.value;
                filterAndRender();
            });
        }

        const pillsWrap = document.getElementById('filter-pills-wrap');
        if (pillsWrap) {
            pillsWrap.addEventListener('click', (e) => {
                const pill = e.target.closest('.filter-pill');
                if (!pill) return;
                activeCategoryId = pill.getAttribute('data-cat');
                pillsWrap.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
                pill.classList.add('active');
                filterAndRender();
            });
        }

        window.clearFilters = function() {
            activeCategoryId = 'all';
            searchQuery = '';
            if (searchInput) searchInput.value = '';
            if (pillsWrap) {
                pillsWrap.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
                const allPill = pillsWrap.querySelector('[data-cat="all"]');
                if (allPill) allPill.classList.add('active');
            }
            filterAndRender();
        };

        filterAndRender();

    } catch (err) {
        console.error('Failed to init all products page:', err);
    }
}

// ==========================================
// 8. HOMEPAGE SERVICES INITIALIZATION
// ==========================================
async function initHomePage() {
    try {
        const data = await fetchCatalogueData();
        const servicesRow = document.querySelector('#services .row.gap-responsive');
        if (servicesRow) {
            // Render dynamic category cards
            servicesRow.innerHTML = data.categories.map(c => `
                <div class="col-12 col-sm-6 col-lg-3">
                    <div class="service-card">
                        <div class="service-image" style="background-image: url('${resolveAssetPath(c.heroImage)}');">
                            <i class="${c.icon} position-absolute top-50 start-50 translate-middle"></i>
                        </div>
                        <h4>${escapeHtml(c.name)} Collection</h4>
                        <p>${escapeHtml(c.description)}</p>
                        <span class="badge bg-light text-dark mb-2">${c.productCount} items</span>
                        <a href="${resolveAssetPath(c.pageUrl)}" class="btn btn-sm btn-outline-primary mt-2">View Collection</a>
                    </div>
                </div>
            `).join('');
        }
        renderSharedContactBlocks();
    } catch (err) {
        console.error('Failed to init homepage services:', err);
    }
}

// ==========================================
// 8B. SHARED CONTACT BLOCK & SOCIAL RENDERER
// ==========================================
function getSharedContactBlockHtml(options = {}) {
    const isFooter = options.variant === 'footer';
    const waUrl = `https://wa.me/${SITE_CONFIG.WHATSAPP_NUMBER}?text=${encodeURIComponent('Hello MSR Tent Mart, I would like to make an enquiry about your event decoration materials.')}`;

    if (isFooter) {
        return `
            <h5>Contact</h5>
            <p class="small text-muted mb-3">Enquire directly via WhatsApp for availability and bookings.</p>
            <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline-light mb-2 w-100 d-inline-flex align-items-center justify-content-center gap-2">
                <i class="fab fa-whatsapp text-success"></i> WhatsApp Enquiry
            </a>
            <p class="small mb-0 text-muted"><i class="fas fa-phone-alt me-2"></i>${escapeHtml(SITE_CONFIG.WHATSAPP_DISPLAY)}</p>
            ${SITE_CONFIG.BUSINESS_EMAIL ? `<p class="small mt-1 mb-0"><a href="mailto:${escapeHtml(SITE_CONFIG.BUSINESS_EMAIL)}" class="text-muted"><i class="fas fa-envelope me-2"></i>${escapeHtml(SITE_CONFIG.BUSINESS_EMAIL)}</a></p>` : ''}
        `;
    }

    return `
        <div class="shared-contact-card p-4 p-md-5 rounded-4 shadow-sm border bg-white text-center">
            <div class="mb-3">
                <i class="fab fa-whatsapp text-success display-4"></i>
            </div>
            <h3 class="h4 fw-bold mb-2">WhatsApp Enquiry</h3>
            <p class="text-muted mb-4">
                Chat with us directly on WhatsApp to check availability, discuss custom requirements, or request pricing for our event decoration items.
            </p>
            <div class="d-flex justify-content-center mb-3">
                <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="btn btn-hero btn-hero-primary d-inline-flex align-items-center justify-content-center gap-2 px-4 py-2">
                    <i class="fab fa-whatsapp fs-5"></i> Enquiry on WhatsApp
                </a>
            </div>
            <p class="fw-semibold text-secondary mb-0">
                <i class="fas fa-phone-alt me-1 text-muted"></i> Direct WhatsApp: <span class="text-dark">${escapeHtml(SITE_CONFIG.WHATSAPP_DISPLAY)}</span>
            </p>
            ${SITE_CONFIG.BUSINESS_EMAIL ? `
            <p class="mt-3 mb-0 text-muted">
                <i class="fas fa-envelope me-1"></i> Reach out on email: <a href="mailto:${escapeHtml(SITE_CONFIG.BUSINESS_EMAIL)}" class="text-decoration-underline text-dark">${escapeHtml(SITE_CONFIG.BUSINESS_EMAIL)}</a>
            </p>
            ` : ''}
        </div>
    `;
}

function renderSharedContactBlocks() {
    document.querySelectorAll('[data-shared-contact]').forEach(el => {
        const variant = el.getAttribute('data-shared-contact');
        el.innerHTML = getSharedContactBlockHtml({ variant });
    });
}

function renderFooterSocial() {
    document.querySelectorAll('.footer-social').forEach(container => {
        let html = '';
        const s = SITE_CONFIG.SOCIAL;
        if (s.instagram) {
            html += `<a href="${escapeHtml(s.instagram)}" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><i class="fab fa-instagram"></i></a>`;
        }
        if (s.facebook) {
            html += `<a href="${escapeHtml(s.facebook)}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>`;
        }
        if (s.linkedin) {
            html += `<a href="${escapeHtml(s.linkedin)}" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>`;
        }
        if (s.youtube) {
            html += `<a href="${escapeHtml(s.youtube)}" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><i class="fab fa-youtube"></i></a>`;
        }
        if (s.other) {
            html += `<a href="${escapeHtml(s.other)}" target="_blank" rel="noopener noreferrer" aria-label="Social Link"><i class="fas fa-link"></i></a>`;
        }
        if (html) {
            container.innerHTML = html;
            container.style.display = 'flex';
        } else {
            container.style.display = 'none';
        }
    });
}

function renderFooterCopyright() {
    document.querySelectorAll('.footer-bottom-row p').forEach(el => {
        el.textContent = `© ${new Date().getFullYear()} ${SITE_CONFIG.BUSINESS_NAME}`;
    });
}

// ==========================================
// 9. SHARED COMPONENTS & NAVIGATION
// ==========================================
async function loadComponents() {
    const basePath = getBasePath();
    const headerPlaceholder = document.getElementById('header-placeholder');
    const footerPlaceholder = document.getElementById('footer-placeholder');

    if (!headerPlaceholder && !footerPlaceholder) {
        renderSharedContactBlocks();
        renderFooterSocial();
        renderFooterCopyright();
        setActiveNavigation();
        return;
    }

    try {
        const fetches = [];
        if (headerPlaceholder) fetches.push(fetch(basePath + 'layout/header.html'));
        if (footerPlaceholder) fetches.push(fetch(basePath + 'layout/footer.html'));

        const responses = await Promise.all(fetches);
        let respIdx = 0;

        if (headerPlaceholder) {
            const hResp = responses[respIdx++];
            if (hResp.ok) {
                const html = await hResp.text();
                headerPlaceholder.innerHTML = html;
                adaptComponentLinks(headerPlaceholder, basePath);
            }
        }

        if (footerPlaceholder) {
            const fResp = responses[respIdx++];
            if (fResp.ok) {
                const html = await fResp.text();
                footerPlaceholder.innerHTML = html;
                adaptComponentLinks(footerPlaceholder, basePath);
            }
        }

        renderSharedContactBlocks();
        renderFooterSocial();
        renderFooterCopyright();
        setActiveNavigation();
    } catch (error) {
        console.error('Error loading shared components:', error);
    }
}

function adaptComponentLinks(container, basePath) {
    if (basePath === './') {
        container.querySelectorAll('[href^="../"], [src^="../"]').forEach(el => {
            if (el.hasAttribute('href')) {
                el.setAttribute('href', el.getAttribute('href').replace(/^\.\.\//, './'));
            }
            if (el.hasAttribute('src')) {
                el.setAttribute('src', el.getAttribute('src').replace(/^\.\.\//, './'));
            }
        });
    }
}

function setActiveNavigation() {
    const path = window.location.pathname;
    const isCategory = path.includes('/categories/');
    const isProducts = path.includes('/products/');
    const isAbout = path.includes('/about/');
    const isContact = path.includes('/contact/');
    const isHome = path.endsWith('/') || (path.endsWith('index.html') && !isCategory && !isProducts && !isAbout && !isContact);

    document.querySelectorAll('.nav-link-desktop').forEach(link => {
        link.classList.remove('active');
        const href = link.getAttribute('href') || '';

        if (isHome) {
            if (href.endsWith('index.html') && !href.includes('#') && !href.includes('/')) {
                link.classList.add('active');
            }
        } else if (isProducts || isCategory) {
            if (href.includes('products/')) {
                link.classList.add('active');
            }
        } else if (isAbout) {
            if (href.includes('about/')) {
                link.classList.add('active');
            }
        } else if (isContact) {
            if (href.includes('contact/')) {
                link.classList.add('active');
            }
        }
    });
}
