document.addEventListener('DOMContentLoaded', () => {
  UI.fillCitySelects();
  UI.fillCategorySelects();
  UI.renderHeader();

  const featured = Store.getAllListings().filter((x) => x.isFeatured).slice(0, 4);
  const latest = Store.getAllListings().slice(0, 6);
  const featuredWrap = document.getElementById('featuredListings');
  const latestWrap = document.getElementById('latestListings');
  featuredWrap.innerHTML = featured.map((x) => UI.listingCard(x)).join('');
  latestWrap.innerHTML = latest.map((x) => UI.listingCard(x)).join('');

  const heroSearch = document.getElementById('heroSearchForm');
  heroSearch?.addEventListener('submit', (e) => {
    e.preventDefault();
    const params = new URLSearchParams({
      q: document.getElementById('heroQuery').value,
      category: document.getElementById('heroCategory').value,
      city: document.getElementById('heroCity').value,
    });
    location.href = `pages/listings.html?${params.toString()}`;
  });
});