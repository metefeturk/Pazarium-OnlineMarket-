document.addEventListener('DOMContentLoaded', () => {
  UI.fillCitySelects();
  UI.fillCategorySelects();
  UI.renderHeader();

  const params = new URLSearchParams(location.search);
  const state = {
    q: params.get('q') || '',
    category: params.get('category') || '',
    city: params.get('city') || '',
    sort: params.get('sort') || 'newest'
  };

  const q = document.getElementById('filterQuery');
  const category = document.getElementById('filterCategory');
  const city = document.getElementById('filterCity');
  const sort = document.getElementById('filterSort');
  q.value = state.q;
  category.value = state.category;
  city.value = state.city;
  sort.value = state.sort;

  const countEl = document.getElementById('listingCount');
  const wrap = document.getElementById('listingGrid');

  function applyFilters() {
    let listings = Store.getAllListings().filter((item) => {
      const text = `${item.title} ${item.description} ${item.brand} ${item.model}`.toLowerCase();
      const textOk = !q.value.trim() || text.includes(q.value.trim().toLowerCase());
      const categoryOk = !category.value || item.category === category.value;
      const cityOk = !city.value || item.city === city.value;
      return textOk && categoryOk && cityOk;
    });

    if (sort.value === 'priceAsc') listings.sort((a,b) => a.price - b.price);
    else if (sort.value === 'priceDesc') listings.sort((a,b) => b.price - a.price);
    else listings.sort((a,b) => String(b.id).localeCompare(String(a.id)));

    countEl.textContent = `${listings.length} ilan bulundu`;
    wrap.innerHTML = listings.length ? listings.map((x) => UI.listingCard(x, '../')).join('') : `<div class="surface empty-state"><h3>Sonuç bulunamadı</h3><p>Filtreleri değiştirip tekrar deneyebilirsin.</p></div>`;
  }

  [q, category, city, sort].forEach((el) => el.addEventListener('input', applyFilters));
  document.getElementById('clearFilters').addEventListener('click', () => {
    q.value = ''; category.value = ''; city.value = ''; sort.value = 'newest'; applyFilters();
  });

  applyFilters();
});