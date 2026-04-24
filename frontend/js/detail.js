document.addEventListener('DOMContentLoaded', () => {
  UI.renderHeader();
  const params = new URLSearchParams(location.search);
  const item = Store.getListingById(params.get('id'));
  if (!item) {
    document.getElementById('detailRoot').innerHTML = `<div class="surface empty-state"><h2>İlan bulunamadı</h2></div>`;
    return;
  }

  let active = 0;
  const main = document.getElementById('mainImage');
  const thumbs = document.getElementById('thumbStrip');
  const title = document.getElementById('detailTitle');
  const price = document.getElementById('detailPrice');
  const description = document.getElementById('detailDescription');
  const specs = document.getElementById('specGrid');
  const seller = document.getElementById('sellerCard');
  const breadcrumbs = document.getElementById('breadcrumbs');

  function renderImage() {
    main.src = UI.resolveImage(item.images[active], '../');
    thumbs.innerHTML = item.images.map((img, idx) => `
      <button class="${idx === active ? 'active' : ''}" data-index="${idx}">
        <img src="${UI.resolveImage(img, "../")}" alt="${item.title}">
      </button>
    `).join('');
    thumbs.querySelectorAll('button').forEach((btn) => btn.addEventListener('click', () => {
      active = Number(btn.dataset.index); renderImage();
    }));
  }

  breadcrumbs.innerHTML = `
    <li>Ana Sayfa</li><li>›</li><li>${UI.getCategoryLabel(item.category)}</li><li>›</li><li>${item.city}</li><li>›</li><li>${item.model}</li>
  `;
  title.textContent = item.title;
  price.textContent = UI.formatPrice(item.price);
  description.textContent = item.description;
  specs.innerHTML = [
    ['Marka', item.brand],
    ['Model', item.model],
    ['Durum', item.status],
    ['Yıl', item.year],
    ['Şehir', item.city],
    ['İlçe', item.district],
  ].map(([k,v]) => `<div class="spec-item"><div class="spec-label">${k}</div><div class="spec-value">${v}</div></div>`).join('');

  seller.innerHTML = `
    <div class="seller-top">
      <div class="avatar">${item.seller.name.split(' ').map((x) => x[0]).slice(0,2).join('')}</div>
      <div>
        <h3 style="margin:0">${item.seller.name}</h3>
        <div class="hint">${item.city} · Üyelik ${item.seller.memberSince}</div>
      </div>
    </div>
    <div class="info-list">
      <div class="info-item"><strong>Telefon:</strong><br>${item.seller.phone}</div>
      <div class="info-item"><strong>Güven Skoru:</strong><br>${item.seller.score} / 5.0</div>
      <div class="info-item"><strong>İlan Durumu:</strong><br>${item.status}</div>
    </div>
    <a class="primary-btn" style="display:block;text-align:center;padding:14px 16px" href="#">Satıcıyla İletişime Geç</a>
    <button class="outline-btn" style="width:100%;margin-top:10px;padding:14px 16px">Favorilere Ekle</button>
  `;

  document.getElementById('prevImage').addEventListener('click', () => { active = (active - 1 + item.images.length) % item.images.length; renderImage(); });
  document.getElementById('nextImage').addEventListener('click', () => { active = (active + 1) % item.images.length; renderImage(); });
  renderImage();

  const similar = Store.getAllListings().filter((x) => x.category === item.category && x.id !== item.id).slice(0, 4);
  document.getElementById('similarGrid').innerHTML = similar.map((x) => UI.listingCard(x, '../')).join('');
  document.getElementById('featureList').innerHTML = item.features.map((x) => `<li class="meta-pill">${x}</li>`).join('');
});