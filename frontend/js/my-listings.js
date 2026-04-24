document.addEventListener('DOMContentLoaded', () => {
  UI.renderHeader();
  const user = Store.getCurrentUser();
  if (!user) {
    UI.toast('Bu alan için giriş yapman gerekiyor.');
    setTimeout(() => location.href = 'login.html', 700);
    return;
  }
  document.getElementById('welcomeUser').textContent = user.fullName;
  const mine = Store.getMyListings();
  document.getElementById('myCount').textContent = mine.length;
  document.getElementById('myCity').textContent = user.city || 'Belirtilmedi';
  document.getElementById('myListingsGrid').innerHTML = mine.length
    ? mine.map((x) => UI.listingCard(x, '../')).join('')
    : `<div class="surface empty-state"><h3>Henüz ilanın yok</h3><p>İlk ilanını vererek vitrine çıkabilirsin.</p><a class="primary-btn" style="display:inline-block;margin-top:12px;padding:13px 16px" href="create-listing.html">İlk İlanını Oluştur</a></div>`;
});