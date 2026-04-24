(function () {
  function formatPrice(value) {
    return new Intl.NumberFormat('tr-TR').format(value) + ' TL';
  }

  function getCategoryLabel(id) {
    return window.APP_DATA.categories.find((c) => c.id === id)?.label || id;
  }

  function fillCitySelects() {
    document.querySelectorAll('[data-cities]').forEach((select) => {
      if (select.dataset.filled === '1') return;
      const first = select.dataset.placeholder || 'Şehir Seç';
      select.innerHTML = `<option value="">${first}</option>` + window.APP_DATA.cities.map((city) => `<option value="${city}">${city}</option>`).join('');
      select.dataset.filled = '1';
    });
  }

  function fillCategorySelects() {
    document.querySelectorAll('[data-categories]').forEach((select) => {
      if (select.dataset.filled === '1') return;
      const first = select.dataset.placeholder || 'Kategori Seç';
      select.innerHTML = `<option value="">${first}</option>` + window.APP_DATA.categories.map((cat) => `<option value="${cat.id}">${cat.label}</option>`).join('');
      select.dataset.filled = '1';
    });
  }

  function renderHeader() {
    const user = window.Store.getCurrentUser();
    document.querySelectorAll('[data-current-user]').forEach((el) => {
      el.textContent = user ? user.fullName.split(' ')[0] : 'Misafir';
    });
    const authArea = document.getElementById('authArea');
    if (!authArea) return;
    authArea.innerHTML = user ? `
      <a class="header-link desktop-only" href="${authArea.dataset.base || ''}pages/my-listings.html">İlanlarım</a>
      <a class="header-link desktop-only" href="${authArea.dataset.base || ''}pages/create-listing.html">Fotoğraf Ekle</a>
      <button class="header-link" id="logoutBtn">Çıkış</button>
      <a class="primary-btn" href="${authArea.dataset.base || ''}pages/create-listing.html">Ücretsiz İlan Ver</a>
    ` : `
      <a class="header-link" href="${authArea.dataset.base || ''}pages/login.html">Giriş Yap</a>
      <a class="header-link desktop-only" href="${authArea.dataset.base || ''}pages/register.html">Hesap Aç</a>
      <a class="primary-btn" href="${authArea.dataset.base || ''}pages/register.html">Ücretsiz İlan Ver</a>
    `;
    document.getElementById('logoutBtn')?.addEventListener('click', () => {
      window.Store.logout();
      location.href = (authArea.dataset.base || '') + 'index.html';
    });
  }

  function toast(message) {
    let el = document.querySelector('.toast');
    if (!el) {
      el = document.createElement('div');
      el.className = 'toast';
      document.body.appendChild(el);
    }
    el.textContent = message;
    el.classList.add('show');
    clearTimeout(el._timer);
    el._timer = setTimeout(() => el.classList.remove('show'), 2600);
  }

  function resolveImage(path, base = '') {
    if (!path) return '';
    return String(path).startsWith('data:') ? path : `${base}${path}`;
  }

  function listingCard(item, base = '') {
    return `
      <article class="listing-card sidebar-card">
        <div class="card-media">
          <span class="label-chip">${item.label || 'İlan'}</span>
          ${item.status ? `<span class="status-chip">${item.status}</span>` : ''}
          <span class="favorite-chip">❤</span>
          <img src="${resolveImage(item.images[0], base)}" alt="${item.title}">
        </div>
        <div class="card-body">
          <div class="ribbon-note">${item.publishedAt} · ${item.city}</div>
          <h3 class="card-title">${item.title}</h3>
          <div class="price-row">
            <div>
              <div class="price">${formatPrice(item.price)}</div>
              ${item.oldPrice ? `<div class="old-price">${formatPrice(item.oldPrice)}</div>` : ''}
            </div>
          </div>
          <div class="meta-row">
            <span class="meta-pill">${getCategoryLabel(item.category)}</span>
            <span class="meta-pill">${item.district}</span>
            <span class="meta-pill">${item.condition}</span>
          </div>
          <div class="meta-row">
            ${(item.features || []).slice(0, 2).map((x) => `<span class="meta-pill">${x}</span>`).join('')}
          </div>
          <div class="card-actions">
            <a class="outline-btn" href="${base}pages/detail.html?id=${item.id}">Detaylar</a>
            <a class="primary-btn" href="${base}pages/detail.html?id=${item.id}">İncele</a>
          </div>
        </div>
      </article>
    `;
  }

  window.UI = { formatPrice, getCategoryLabel, fillCitySelects, fillCategorySelects, renderHeader, toast, listingCard, resolveImage };
})();