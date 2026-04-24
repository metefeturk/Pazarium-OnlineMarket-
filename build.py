from pathlib import Path
import textwrap, json, os
base = Path('/mnt/data/marketpro/frontend')

files = {}
files['css/style.css'] = r'''
:root {
  --yellow: #ffd400;
  --yellow-dark: #f2c300;
  --blue: #2f6fed;
  --blue-deep: #1d4ed8;
  --text: #20242c;
  --muted: #667085;
  --line: #e5e7eb;
  --bg: #f5f7fb;
  --card: #ffffff;
  --success: #13a663;
  --danger: #da3a32;
  --shadow: 0 10px 30px rgba(16, 24, 40, 0.08);
  --radius: 18px;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: Inter, Arial, Helvetica, sans-serif;
  color: var(--text);
  background:
    radial-gradient(circle at top right, rgba(47,111,237,.14), transparent 22%),
    radial-gradient(circle at top left, rgba(255,212,0,.16), transparent 22%),
    var(--bg);
}
a { color: inherit; text-decoration: none; }
img { max-width: 100%; display: block; }
button, input, select, textarea { font: inherit; }
.container { width: min(1280px, calc(100% - 32px)); margin: 0 auto; }
.topbar {
  background: linear-gradient(90deg, #fff9cf, #fef3a8);
  border-bottom: 1px solid rgba(0,0,0,.05);
  padding: 9px 0;
  font-size: 13px;
  color: #5e5320;
}
.topbar .container, .main-header .container, .hero-search, .content-grid, .page-grid, .detail-layout, .footer-grid, .account-summary {
  display: flex;
  gap: 16px;
}
.topbar .container { justify-content: space-between; align-items: center; }
.main-header {
  position: sticky; top: 0; z-index: 20;
  backdrop-filter: blur(16px);
  background: rgba(255,255,255,.82);
  border-bottom: 1px solid rgba(15,23,42,.06);
}
.main-header .container { align-items: center; padding: 14px 0; }
.brand {
  display: flex; align-items: center; gap: 12px; min-width: 200px;
}
.brand-logo {
  width: 44px; height: 44px; border-radius: 14px;
  background: linear-gradient(135deg, var(--yellow), #ffec8a 45%, white 46%, var(--blue) 100%);
  box-shadow: var(--shadow);
  position: relative;
  overflow: hidden;
}
.brand-logo::after {
  content: ""; position: absolute; inset: 7px; border-radius: 10px;
  background: rgba(255,255,255,.38); border: 1px solid rgba(255,255,255,.5);
}
.brand-title { font-weight: 800; font-size: 20px; letter-spacing: -.3px; }
.brand-subtitle { color: var(--muted); font-size: 12px; margin-top: 2px; }
.header-search {
  flex: 1; display: grid; grid-template-columns: 1fr 140px 150px 56px; gap: 10px;
  background: rgba(255,255,255,.92); border: 1px solid rgba(15,23,42,.06);
  padding: 10px; border-radius: 20px; box-shadow: var(--shadow);
}
.input-like, .header-search input, .header-search select, .filter-bar input, .filter-bar select, .form-grid input, .form-grid textarea, .form-grid select {
  border: 1px solid var(--line);
  background: #fff;
  border-radius: 14px;
  padding: 13px 14px;
  transition: .2s ease;
}
.header-search input:focus, .header-search select:focus, .filter-bar input:focus, .filter-bar select:focus, .form-grid input:focus, .form-grid textarea:focus, .form-grid select:focus {
  outline: none; border-color: rgba(47,111,237,.45); box-shadow: 0 0 0 4px rgba(47,111,237,.12);
}
.search-btn, .primary-btn, .ghost-btn, .outline-btn, .pill-btn {
  border: none; cursor: pointer; border-radius: 14px; font-weight: 700; transition: .22s ease;
}
.search-btn, .primary-btn {
  background: linear-gradient(135deg, var(--blue), var(--blue-deep)); color: #fff;
  box-shadow: 0 12px 30px rgba(47,111,237,.25);
}
.search-btn:hover, .primary-btn:hover { transform: translateY(-2px); }
.header-actions { display: flex; gap: 10px; align-items: center; }
.header-link, .outline-btn, .ghost-btn {
  padding: 12px 14px; border: 1px solid rgba(15,23,42,.08); background: rgba(255,255,255,.85);
}
.primary-btn { padding: 14px 18px; }
.pill-btn {
  padding: 11px 14px; background: linear-gradient(90deg, #fff, #f9fafb);
  border: 1px solid rgba(15,23,42,.06);
}
.hero {
  padding: 36px 0 24px;
}
.hero-card {
  position: relative; overflow: hidden; border-radius: 30px; min-height: 420px;
  background: linear-gradient(120deg, #18253f 0%, #213b71 35%, #335fbb 68%, #7398eb 100%);
  box-shadow: 0 20px 60px rgba(17, 24, 39, .18);
}
.hero-card::before, .hero-card::after {
  content: ""; position: absolute; border-radius: 999px; filter: blur(8px); opacity: .55;
  animation: floatBlob 8s ease-in-out infinite;
}
.hero-card::before { width: 280px; height: 280px; right: -40px; top: -50px; background: rgba(255,212,0,.28); }
.hero-card::after { width: 320px; height: 320px; left: -80px; bottom: -120px; background: rgba(255,255,255,.09); animation-delay: -3s; }
@keyframes floatBlob { 50% { transform: translateY(18px) translateX(-12px) scale(1.04); } }
.hero-inner {
  position: relative; z-index: 1; display: grid; grid-template-columns: 1.15fr .85fr; gap: 26px; align-items: center;
  padding: 42px;
}
.hero-copy { color: white; }
.eyebrow {
  display: inline-flex; gap: 10px; align-items: center; padding: 10px 14px; border-radius: 999px;
  background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.14); font-size: 13px;
}
.hero-copy h1 {
  margin: 18px 0 14px; font-size: clamp(32px, 5vw, 56px); line-height: 1.04; letter-spacing: -1.6px;
}
.hero-copy p { margin: 0; color: rgba(255,255,255,.82); font-size: 17px; line-height: 1.65; max-width: 680px; }
.hero-stats {
  display: grid; grid-template-columns: repeat(3,1fr); gap: 12px; margin-top: 22px;
}
.stat-card {
  background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.12);
  border-radius: 18px; padding: 16px;
}
.stat-value { color: #fff; font-size: 22px; font-weight: 800; }
.stat-label { color: rgba(255,255,255,.72); font-size: 13px; margin-top: 4px; }
.hero-panel {
  background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.14); padding: 18px; border-radius: 24px;
  backdrop-filter: blur(12px);
}
.hero-panel img { border-radius: 18px; aspect-ratio: 4 / 3; object-fit: cover; }
.hero-panel h3 { color: #fff; margin: 14px 0 8px; font-size: 24px; }
.hero-panel p { color: rgba(255,255,255,.78); margin: 0 0 14px; line-height: 1.6; }
.badges { display: flex; gap: 10px; flex-wrap: wrap; }
.badge {
  background: rgba(255,255,255,.14); color: #fff; padding: 9px 11px; border-radius: 999px; font-size: 12px; border: 1px solid rgba(255,255,255,.12);
}
.section { padding: 22px 0; }
.section-head {
  display: flex; justify-content: space-between; align-items: end; gap: 18px; margin-bottom: 16px;
}
.section-title { margin: 0; font-size: 28px; letter-spacing: -.8px; }
.section-subtitle { margin: 6px 0 0; color: var(--muted); line-height: 1.6; }
.content-grid {
  align-items: start;
}
.sidebar {
  width: 280px; flex: 0 0 280px; position: sticky; top: 90px;
}
.sidebar-card, .surface, .detail-card, .seller-card, .mini-card {
  background: rgba(255,255,255,.92); border: 1px solid rgba(15,23,42,.06); box-shadow: var(--shadow); border-radius: 24px;
}
.sidebar-card { padding: 18px; }
.sidebar h3 { margin: 0 0 16px; font-size: 18px; }
.category-list, .feature-list, .breadcrumbs, .spec-list, .bullet-list { list-style: none; padding: 0; margin: 0; }
.category-list a {
  display: flex; justify-content: space-between; align-items: center; padding: 11px 12px; border-radius: 14px;
  color: #243041; transition: .2s ease;
}
.category-list a:hover, .category-list a.active { background: #f4f7ff; color: var(--blue); transform: translateX(2px); }
.page-main { flex: 1; min-width: 0; }
.filter-bar {
  display: grid; grid-template-columns: 1.2fr repeat(4, 1fr) 54px; gap: 12px;
  background: rgba(255,255,255,.92); padding: 14px; border-radius: 22px; border: 1px solid rgba(15,23,42,.06); box-shadow: var(--shadow);
  margin-bottom: 18px;
}
.filter-icon {
  display: grid; place-items: center; background: linear-gradient(135deg, var(--yellow), #ffe46f);
}
.grid-cards {
  display: grid; grid-template-columns: repeat(3, minmax(0,1fr)); gap: 18px;
}
.listing-card {
  overflow: hidden; position: relative; transition: .25s ease; display: flex; flex-direction: column;
}
.listing-card:hover { transform: translateY(-5px); }
.card-media {
  position: relative; overflow: hidden; aspect-ratio: 16 / 11; background: #e8edf6;
}
.card-media img { width: 100%; height: 100%; object-fit: cover; transition: .45s ease; }
.listing-card:hover .card-media img { transform: scale(1.04); }
.favorite-chip, .label-chip, .status-chip {
  position: absolute; top: 14px; z-index: 1; padding: 9px 11px; border-radius: 999px; font-size: 12px; font-weight: 700;
}
.favorite-chip { right: 14px; background: rgba(255,255,255,.88); backdrop-filter: blur(8px); }
.label-chip { left: 14px; background: rgba(255,212,0,.94); color: #513f00; }
.status-chip { right: 62px; background: rgba(19,166,99,.92); color: #fff; }
.card-body { padding: 18px; display: flex; flex-direction: column; gap: 10px; flex: 1; }
.card-title { margin: 0; font-size: 18px; line-height: 1.35; }
.price-row { display: flex; justify-content: space-between; align-items: center; gap: 10px; }
.price { font-size: 28px; font-weight: 800; letter-spacing: -.7px; }
.old-price { color: #98a2b3; text-decoration: line-through; font-size: 14px; }
.meta-row {
  display: flex; flex-wrap: wrap; gap: 8px; color: var(--muted); font-size: 13px;
}
.meta-pill {
  padding: 8px 10px; border-radius: 999px; background: #f7f8fb; border: 1px solid #edf0f5;
}
.card-actions { display: flex; gap: 10px; margin-top: auto; }
.card-actions .outline-btn, .card-actions .primary-btn { flex: 1; text-align: center; padding: 12px 14px; }
.ribbon-note {
  display: inline-flex; gap: 8px; align-items: center; padding: 8px 10px; border-radius: 999px;
  color: #6b5c00; background: #fff8cc; font-size: 12px; font-weight: 700; border: 1px solid rgba(0,0,0,.05);
}
.page-hero {
  padding: 26px 0 10px;
}
.page-grid, .detail-layout { align-items: start; }
.page-grid .sidebar { top: 100px; }
.account-summary {
  justify-content: space-between; align-items: stretch; margin-bottom: 18px;
}
.summary-tile {
  flex: 1; padding: 18px; border-radius: 22px; background: rgba(255,255,255,.95); border: 1px solid rgba(15,23,42,.06); box-shadow: var(--shadow);
}
.summary-tile .value { font-size: 28px; font-weight: 800; margin-top: 8px; }
.empty-state {
  padding: 32px; text-align: center; color: var(--muted);
}
.form-shell {
  display: grid; grid-template-columns: 1fr 360px; gap: 20px;
}
.form-card { padding: 24px; }
.form-grid {
  display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px;
}
.form-grid .full { grid-column: 1 / -1; }
.form-grid textarea { min-height: 140px; resize: vertical; }
.dropzone {
  border: 2px dashed rgba(47,111,237,.22); background: linear-gradient(180deg, #f8fbff, #fff); padding: 20px; border-radius: 20px;
}
.dropzone.dragover { border-color: rgba(47,111,237,.55); background: #eef5ff; }
.upload-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-top: 14px; }
.upload-thumb { position: relative; border-radius: 18px; overflow: hidden; aspect-ratio: 1; background: #eff3f8; }
.upload-thumb img { width: 100%; height: 100%; object-fit: cover; }
.remove-thumb {
  position: absolute; top: 8px; right: 8px; border: none; width: 32px; height: 32px; border-radius: 50%; background: rgba(32,36,44,.82); color: #fff; cursor: pointer;
}
.hint { color: var(--muted); font-size: 13px; line-height: 1.6; }
.detail-layout { display: grid; grid-template-columns: minmax(0, 1fr) 360px; gap: 20px; }
.detail-main { min-width: 0; }
.detail-card { padding: 20px; }
.gallery-main {
  border-radius: 24px; overflow: hidden; aspect-ratio: 16 / 10; background: #eef2f6; position: relative;
}
.gallery-main img { width: 100%; height: 100%; object-fit: cover; }
.gallery-nav {
  position: absolute; inset: auto 16px 16px auto; display: flex; gap: 10px;
}
.gallery-btn {
  width: 46px; height: 46px; border-radius: 50%; border: none; background: rgba(255,255,255,.88); cursor: pointer; box-shadow: var(--shadow);
}
.thumb-strip {
  display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-top: 12px;
}
.thumb-strip button {
  border: none; padding: 0; border-radius: 16px; overflow: hidden; cursor: pointer; aspect-ratio: 1.2;
  border: 2px solid transparent; background: #eef2f6;
}
.thumb-strip button.active { border-color: var(--blue); }
.thumb-strip img { width: 100%; height: 100%; object-fit: cover; }
.detail-head { display: flex; justify-content: space-between; gap: 20px; align-items: start; margin-top: 18px; }
.detail-title { margin: 0 0 8px; font-size: clamp(28px, 4vw, 40px); letter-spacing: -.9px; }
.detail-price { font-size: 42px; font-weight: 800; }
.breadcrumbs { display: flex; gap: 10px; flex-wrap: wrap; color: var(--muted); font-size: 13px; margin-bottom: 12px; }
.spec-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 20px 0;
}
.spec-item {
  background: #f8fafc; border: 1px solid #edf2f7; border-radius: 18px; padding: 14px;
}
.spec-label { color: var(--muted); font-size: 13px; }
.spec-value { margin-top: 7px; font-weight: 700; }
.description-box { line-height: 1.85; color: #3d4756; }
.seller-card { padding: 20px; position: sticky; top: 92px; }
.seller-top { display: flex; gap: 14px; align-items: center; }
.avatar {
  width: 58px; height: 58px; border-radius: 50%; display: grid; place-items: center;
  background: linear-gradient(135deg, var(--yellow), #fff1a8); font-weight: 800; color: #4e4400;
}
.info-list { display: grid; gap: 12px; margin: 18px 0; }
.info-item { padding: 12px 14px; border-radius: 14px; background: #f8fafc; border: 1px solid #edf2f7; }
.similar-grid { display: grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap: 16px; }
.footer {
  margin-top: 34px; padding: 34px 0 26px; background: linear-gradient(180deg, transparent, rgba(255,255,255,.75)); border-top: 1px solid rgba(15,23,42,.06);
}
.footer-grid { align-items: start; justify-content: space-between; }
.footer small { color: var(--muted); }
.toast {
  position: fixed; right: 18px; bottom: 18px; min-width: 280px; max-width: 420px; padding: 16px 18px; border-radius: 18px;
  background: rgba(32,36,44,.92); color: white; box-shadow: 0 20px 40px rgba(15,23,42,.28); opacity: 0; transform: translateY(10px); pointer-events: none; transition: .25s ease; z-index: 30;
}
.toast.show { opacity: 1; transform: translateY(0); }
.auth-card { width: min(540px, 100%); margin: 12px auto 0; padding: 24px; }
.auth-switch { color: var(--muted); margin-top: 12px; }
.desktop-only { display: inline-flex; }
.mobile-only { display: none; }
@media (max-width: 1180px) {
  .grid-cards, .similar-grid { grid-template-columns: repeat(2, minmax(0,1fr)); }
  .hero-inner, .form-shell, .detail-layout { grid-template-columns: 1fr; }
  .sidebar { display: none; }
  .header-search { grid-template-columns: 1fr 120px 130px 56px; }
  .filter-bar { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 840px) {
  .main-header .container { flex-wrap: wrap; }
  .header-search { order: 3; width: 100%; grid-template-columns: 1fr 1fr 1fr 56px; }
  .hero-card { min-height: auto; }
  .hero-copy h1 { font-size: 34px; }
  .grid-cards, .similar-grid, .spec-grid, .upload-grid, .hero-stats, .thumb-strip, .form-grid { grid-template-columns: 1fr; }
  .section-head, .footer-grid, .account-summary, .topbar .container { flex-direction: column; align-items: flex-start; }
  .header-actions { width: 100%; flex-wrap: wrap; }
  .desktop-only { display: none; }
  .mobile-only { display: inline-flex; }
  .filter-bar { grid-template-columns: 1fr; }
}
'''

files['js/data.js'] = r'''
window.APP_DATA = {
  cities: [
    "İstanbul", "Ankara", "İzmir", "Bursa", "Antalya", "Adana", "Konya", "Gaziantep", "Kocaeli", "Mersin", "Samsun", "Trabzon", "Kayseri", "Eskişehir", "Muğla", "Balıkesir", "Kastamonu"
  ],
  categories: [
    { id: "telefon", label: "Cep Telefonu" },
    { id: "bilgisayar", label: "Bilgisayar" },
    { id: "vasita", label: "Vasıta" },
    { id: "ev-esyasi", label: "Ev Eşyası" },
    { id: "kamera", label: "Fotoğraf & Kamera" },
    { id: "oyuncu", label: "Oyuncu Ekipmanları" },
    { id: "spor", label: "Spor & Outdoor" },
    { id: "mobilya", label: "Mobilya" }
  ],
  demoUser: {
    id: "demo-user-1",
    fullName: "Metehan E.",
    email: "demo@pazarium.com",
    phone: "0532 000 00 00",
    city: "Kastamonu"
  },
  listings: [
    {
      id: "l1",
      title: "iPhone 14 Pro 128 GB - Hatasız, Kutu Faturalı",
      price: 42950,
      oldPrice: 44800,
      category: "telefon",
      city: "İstanbul",
      district: "Kadıköy",
      label: "Öne Çıkan",
      condition: "İkinci El",
      brand: "Apple",
      model: "iPhone 14 Pro",
      year: 2023,
      status: "Yeni Gibi",
      description: "Cihaz tertemiz kullanıldı. Kozmetik olarak çok iyi durumda, ekranında kırık ya da çatlak yok. Pil sağlığı iyi seviyede. Kutu, kablo ve fatura mevcut. Elden teslim önceliklidir.",
      seller: { name: "Selin Kaya", phone: "0554 210 66 91", memberSince: "2021", score: 4.9 },
      images: ["assets/images/phone-1.svg", "assets/images/phone-2.svg", "assets/images/phone-3.svg"],
      features: ["Face ID", "128 GB", "Pil Sağlığı %89", "Türkiye Cihazı"],
      publishedAt: "Bugün",
      isFeatured: true,
      ownerId: "seed-1"
    },
    {
      id: "l2",
      title: "MacBook Air M2 13.6 - 8/256 - Çok Temiz",
      price: 33600,
      oldPrice: 34990,
      category: "bilgisayar",
      city: "Ankara",
      district: "Çankaya",
      label: "Hızlı Satış",
      condition: "İkinci El",
      brand: "Apple",
      model: "MacBook Air M2",
      year: 2024,
      status: "Yeni Gibi",
      description: "Ofis kullanımı için alındı. Sadece birkaç ay kullanıldı. Şarj döngüsü düşük, kozmetik kusursuz. Kutu ve aksesuarları tam.",
      seller: { name: "Eren Bilgiç", phone: "0543 111 10 10", memberSince: "2020", score: 4.8 },
      images: ["assets/images/laptop-1.svg", "assets/images/laptop-2.svg", "assets/images/laptop-3.svg"],
      features: ["M2 İşlemci", "Retina Ekran", "8 GB RAM", "256 GB SSD"],
      publishedAt: "Dün",
      isFeatured: true,
      ownerId: "seed-2"
    },
    {
      id: "l3",
      title: "Volkswagen Golf 1.5 TSI Life DSG - Boyasız",
      price: 1195000,
      oldPrice: 1230000,
      category: "vasita",
      city: "İzmir",
      district: "Bornova",
      label: "Kurumsal",
      condition: "İkinci El",
      brand: "Volkswagen",
      model: "Golf",
      year: 2022,
      status: "Ekspertiz Hazır",
      description: "Araçta değişen yoktur. Düzenli servis bakımlı, düşük kilometreli ve masrafsızdır. İstenilen serviste ekspertize açıktır.",
      seller: { name: "Altın Yol Otomotiv", phone: "0536 887 44 00", memberSince: "2018", score: 5.0 },
      images: ["assets/images/car-1.svg", "assets/images/car-2.svg", "assets/images/car-3.svg"],
      features: ["79.000 km", "Otomatik", "Benzin", "Yetkili Servis Bakımlı"],
      publishedAt: "2 gün önce",
      isFeatured: true,
      ownerId: "seed-3"
    },
    {
      id: "l4",
      title: "L Koltuk Takımı - Yıkanabilir Kumaş - Az Kullanıldı",
      price: 18400,
      oldPrice: 19900,
      category: "mobilya",
      city: "Bursa",
      district: "Nilüfer",
      label: "Fırsat",
      condition: "İkinci El",
      brand: "Vivense",
      model: "L Koltuk",
      year: 2023,
      status: "Temiz",
      description: "Salon değişikliği nedeniyle satılıktır. Kumaşı sökülüp yıkanabiliyor. Çökme, yırtık veya leke yok. Ölçüler detayda paylaşılır.",
      seller: { name: "Ayşe Şimşek", phone: "0531 224 12 31", memberSince: "2022", score: 4.7 },
      images: ["assets/images/sofa-1.svg", "assets/images/sofa-2.svg", "assets/images/sofa-3.svg"],
      features: ["Yıkanabilir Kumaş", "Modern Tasarım", "Geniş Oturum", "Az Kullanıldı"],
      publishedAt: "3 gün önce",
      isFeatured: false,
      ownerId: "seed-4"
    },
    {
      id: "l5",
      title: "Sony A7 III + 28-70 Lens - Shutter Düşük",
      price: 51400,
      oldPrice: 53250,
      category: "kamera",
      city: "Antalya",
      district: "Muratpaşa",
      label: "Vitrin",
      condition: "İkinci El",
      brand: "Sony",
      model: "A7 III",
      year: 2023,
      status: "Profesyonel",
      description: "Fotoğraf stüdyosunda yedek gövde olarak kullanıldı. Shutter düşük, kozmetik temiz. Lens ve batarya dahil. İstenirse örnek çekim paylaşılır.",
      seller: { name: "Mert Yalın", phone: "0544 901 20 00", memberSince: "2019", score: 4.9 },
      images: ["assets/images/camera-1.svg", "assets/images/camera-2.svg", "assets/images/camera-3.svg"],
      features: ["Full Frame", "4K Video", "Düşük Shutter", "Lens Dahil"],
      publishedAt: "4 gün önce",
      isFeatured: true,
      ownerId: "seed-5"
    },
    {
      id: "l6",
      title: "PlayStation 5 Slim + 2 Kol + FIFA 25",
      price: 23900,
      oldPrice: 24990,
      category: "oyuncu",
      city: "Kocaeli",
      district: "İzmit",
      label: "Kaçırma",
      condition: "İkinci El",
      brand: "Sony",
      model: "PS5 Slim",
      year: 2024,
      status: "Temiz",
      description: "Evde özenli kullanıldı. 2 orijinal kol ve oyun hesabı ile teslim edilecek. Kutusu mevcut, cihazda hiçbir sorun yok.",
      seller: { name: "Can Güneş", phone: "0507 980 45 45", memberSince: "2023", score: 4.6 },
      images: ["assets/images/console-1.svg", "assets/images/console-2.svg", "assets/images/console-3.svg"],
      features: ["2 Kol", "Kutulu", "Oyun Dahil", "Temiz Kullanım"],
      publishedAt: "5 gün önce",
      isFeatured: false,
      ownerId: "seed-6"
    },
    {
      id: "l7",
      title: "Elektrikli Katlanır Bisiklet - 45 km Menzil",
      price: 27150,
      oldPrice: 28500,
      category: "spor",
      city: "Eskişehir",
      district: "Tepebaşı",
      label: "Yeni İlan",
      condition: "İkinci El",
      brand: "Volta",
      model: "VSM",
      year: 2024,
      status: "Bakımlı",
      description: "Şehir içi kullanım için idealdir. Katlanabilir yapıdadır. Batarya sağlığı iyi, lastikler yenidir. Şarj cihazı ile verilecektir.",
      seller: { name: "Burak Çelik", phone: "0535 772 22 19", memberSince: "2021", score: 4.8 },
      images: ["assets/images/bike-1.svg", "assets/images/bike-2.svg", "assets/images/bike-3.svg"],
      features: ["45 km Menzil", "Katlanabilir", "Şarj Cihazı Dahil", "Bakımlı"],
      publishedAt: "1 hafta önce",
      isFeatured: false,
      ownerId: "seed-7"
    },
    {
      id: "l8",
      title: "Samsung 55'' 4K Smart TV - Kumandalı",
      price: 17200,
      oldPrice: 18150,
      category: "ev-esyasi",
      city: "Trabzon",
      district: "Ortahisar",
      label: "Öne Çıkan",
      condition: "İkinci El",
      brand: "Samsung",
      model: "55AU9000",
      year: 2022,
      status: "Çiziksiz",
      description: "Taşınma nedeniyle satılıyor. Panel sorunsuz, ölü piksel yok. Kumanda ve ayakları mevcut. İstenirse duvar aparatı da verilir.",
      seller: { name: "Zeynep Kılıç", phone: "0532 770 33 88", memberSince: "2020", score: 4.9 },
      images: ["assets/images/tv-1.svg", "assets/images/tv-2.svg", "assets/images/tv-3.svg"],
      features: ["4K UHD", "Smart TV", "Wi‑Fi", "Kumandalı"],
      publishedAt: "1 hafta önce",
      isFeatured: true,
      ownerId: "seed-8"
    }
  ]
};
'''

files['js/store.js'] = r'''
(function () {
  const STORAGE_KEYS = {
    users: 'pazarium_users',
    currentUser: 'pazarium_current_user',
    listings: 'pazarium_user_listings'
  };

  const clone = (x) => JSON.parse(JSON.stringify(x));

  function getUsers() {
    const raw = localStorage.getItem(STORAGE_KEYS.users);
    if (raw) return JSON.parse(raw);
    const seed = [window.APP_DATA.demoUser];
    localStorage.setItem(STORAGE_KEYS.users, JSON.stringify(seed));
    return seed;
  }

  function saveUsers(users) {
    localStorage.setItem(STORAGE_KEYS.users, JSON.stringify(users));
  }

  function getCurrentUser() {
    const raw = localStorage.getItem(STORAGE_KEYS.currentUser);
    return raw ? JSON.parse(raw) : window.APP_DATA.demoUser;
  }

  function setCurrentUser(user) {
    localStorage.setItem(STORAGE_KEYS.currentUser, JSON.stringify(user));
  }

  function logout() {
    localStorage.removeItem(STORAGE_KEYS.currentUser);
  }

  function getUserListings() {
    const raw = localStorage.getItem(STORAGE_KEYS.listings);
    return raw ? JSON.parse(raw) : [];
  }

  function saveUserListings(listings) {
    localStorage.setItem(STORAGE_KEYS.listings, JSON.stringify(listings));
  }

  function getAllListings() {
    return [...clone(window.APP_DATA.listings), ...getUserListings()]
      .sort((a, b) => String(b.id).localeCompare(String(a.id)));
  }

  function createListing(payload) {
    const user = getCurrentUser() || window.APP_DATA.demoUser;
    const current = getUserListings();
    const listing = {
      id: `u-${Date.now()}`,
      ownerId: user.id,
      seller: {
        name: user.fullName,
        phone: user.phone || 'Belirtilmedi',
        memberSince: '2026',
        score: 5.0
      },
      publishedAt: 'Az önce',
      isFeatured: false,
      ...payload
    };
    current.unshift(listing);
    saveUserListings(current);
    return listing;
  }

  function registerUser(payload) {
    const users = getUsers();
    const exists = users.find((u) => u.email.toLowerCase() === payload.email.toLowerCase());
    if (exists) {
      return { ok: false, message: 'Bu e-posta ile kayıtlı bir hesap zaten var.' };
    }
    const user = {
      id: `usr-${Date.now()}`,
      fullName: payload.fullName,
      email: payload.email,
      phone: payload.phone,
      city: payload.city
    };
    users.push({ ...user, password: payload.password });
    saveUsers(users);
    setCurrentUser(user);
    return { ok: true, user };
  }

  function loginUser(email, password) {
    const users = getUsers();
    const match = users.find((u) => u.email.toLowerCase() === email.toLowerCase() && u.password === password);
    if (!match) return { ok: false, message: 'E-posta veya şifre hatalı.' };
    const safeUser = { id: match.id, fullName: match.fullName, email: match.email, phone: match.phone, city: match.city };
    setCurrentUser(safeUser);
    return { ok: true, user: safeUser };
  }

  function getMyListings() {
    const user = getCurrentUser();
    if (!user) return [];
    return getAllListings().filter((x) => x.ownerId === user.id);
  }

  function getListingById(id) {
    return getAllListings().find((x) => x.id === id);
  }

  window.Store = {
    getUsers,
    getCurrentUser,
    setCurrentUser,
    logout,
    getAllListings,
    createListing,
    registerUser,
    loginUser,
    getMyListings,
    getListingById,
    getUserListings
  };
})();
'''

files['js/ui.js'] = r'''
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

  function listingCard(item, base = '') {
    return `
      <article class="listing-card sidebar-card">
        <div class="card-media">
          <span class="label-chip">${item.label || 'İlan'}</span>
          ${item.status ? `<span class="status-chip">${item.status}</span>` : ''}
          <span class="favorite-chip">❤</span>
          <img src="${base}${item.images[0]}" alt="${item.title}">
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

  window.UI = { formatPrice, getCategoryLabel, fillCitySelects, fillCategorySelects, renderHeader, toast, listingCard };
})();
'''

files['js/main.js'] = r'''
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
'''

files['js/listings.js'] = r'''
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
'''

files['js/detail.js'] = r'''
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
    main.src = `../${item.images[active]}`;
    thumbs.innerHTML = item.images.map((img, idx) => `
      <button class="${idx === active ? 'active' : ''}" data-index="${idx}">
        <img src="../${img}" alt="${item.title}">
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
'''

files['js/create-listing.js'] = r'''
document.addEventListener('DOMContentLoaded', () => {
  UI.renderHeader();
  UI.fillCitySelects();
  UI.fillCategorySelects();

  const form = document.getElementById('listingForm');
  const input = document.getElementById('images');
  const preview = document.getElementById('uploadPreview');
  const dropzone = document.getElementById('dropzone');
  const filesBuffer = [];

  const user = Store.getCurrentUser();
  if (!user) {
    UI.toast('İlan eklemek için önce giriş yapman gerekiyor.');
    setTimeout(() => location.href = 'login.html', 700);
    return;
  }

  function readFiles(fileList) {
    [...fileList].slice(0, 6 - filesBuffer.length).forEach((file) => {
      if (!file.type.startsWith('image/')) return;
      const reader = new FileReader();
      reader.onload = () => {
        filesBuffer.push({ name: file.name, dataUrl: reader.result });
        renderPreview();
      };
      reader.readAsDataURL(file);
    });
  }

  function renderPreview() {
    preview.innerHTML = filesBuffer.map((f, i) => `
      <div class="upload-thumb">
        <img src="${f.dataUrl}" alt="${f.name}">
        <button type="button" class="remove-thumb" data-index="${i}">×</button>
      </div>
    `).join('');
    preview.querySelectorAll('.remove-thumb').forEach((btn) => btn.addEventListener('click', () => {
      filesBuffer.splice(Number(btn.dataset.index), 1);
      renderPreview();
    }));
  }

  input.addEventListener('change', (e) => readFiles(e.target.files));
  ;['dragenter', 'dragover'].forEach((evt) => dropzone.addEventListener(evt, (e) => { e.preventDefault(); dropzone.classList.add('dragover'); }));
  ;['dragleave', 'drop'].forEach((evt) => dropzone.addEventListener(evt, (e) => { e.preventDefault(); dropzone.classList.remove('dragover'); }));
  dropzone.addEventListener('drop', (e) => readFiles(e.dataTransfer.files));

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!filesBuffer.length) {
      UI.toast('En az bir fotoğraf eklemelisin.');
      return;
    }
    const listing = Store.createListing({
      title: document.getElementById('title').value,
      price: Number(document.getElementById('price').value),
      oldPrice: Number(document.getElementById('oldPrice').value) || null,
      category: document.getElementById('category').value,
      city: document.getElementById('city').value,
      district: document.getElementById('district').value,
      condition: document.getElementById('condition').value,
      brand: document.getElementById('brand').value,
      model: document.getElementById('model').value,
      year: document.getElementById('year').value,
      status: document.getElementById('status').value,
      label: document.getElementById('label').value || 'Yeni İlan',
      description: document.getElementById('description').value,
      features: document.getElementById('features').value.split(',').map((x) => x.trim()).filter(Boolean),
      images: filesBuffer.map((x) => x.dataUrl)
    });
    UI.toast('İlanın başarıyla oluşturuldu.');
    setTimeout(() => location.href = `detail.html?id=${listing.id}`, 800);
  });
});
'''

files['js/auth.js'] = r'''
document.addEventListener('DOMContentLoaded', () => {
  UI.renderHeader();
  UI.fillCitySelects();

  const registerForm = document.getElementById('registerForm');
  const loginForm = document.getElementById('loginForm');

  registerForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    const result = Store.registerUser({
      fullName: document.getElementById('fullName').value,
      email: document.getElementById('registerEmail').value,
      password: document.getElementById('registerPassword').value,
      phone: document.getElementById('phone').value,
      city: document.getElementById('city').value,
    });
    if (!result.ok) return UI.toast(result.message);
    UI.toast('Hesabın oluşturuldu.');
    setTimeout(() => location.href = 'my-listings.html', 700);
  });

  loginForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    const result = Store.loginUser(
      document.getElementById('loginEmail').value,
      document.getElementById('loginPassword').value
    );
    if (!result.ok) return UI.toast(result.message);
    UI.toast('Giriş başarılı.');
    setTimeout(() => location.href = 'my-listings.html', 700);
  });
});
'''

files['js/my-listings.js'] = r'''
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
'''

header = '''
<div class="topbar">
  <div class="container">
    <div>Detaylı arama · Güvenli alışveriş deneyimi · Profesyonel pazar yeri vitrini</div>
    <div>Hoş geldin, <strong data-current-user>Misafir</strong></div>
  </div>
</div>
<header class="main-header">
  <div class="container">
    <a class="brand" href="{base}index.html">
      <div class="brand-logo"></div>
      <div>
        <div class="brand-title">Pazarium</div>
        <div class="brand-subtitle">İkinci el alım satım platformu</div>
      </div>
    </a>
    <form class="header-search" action="{base}pages/listings.html">
      <input type="text" name="q" placeholder="Ne aramıştın? Telefon, araç, bilgisayar...">
      <select name="category" data-categories data-placeholder="Kategori"></select>
      <select name="city" data-cities data-placeholder="Şehir"></select>
      <button class="search-btn" aria-label="Ara">⌕</button>
    </form>
    <div class="header-actions" id="authArea" data-base="{base}"></div>
  </div>
</header>
'''

footer = '''
<footer class="footer">
  <div class="container footer-grid">
    <div>
      <div class="brand" style="min-width:auto">
        <div class="brand-logo"></div>
        <div>
          <div class="brand-title">Pazarium</div>
          <div class="brand-subtitle">Profesyonel ikinci el pazar yeri prototipi</div>
        </div>
      </div>
      <small>Bu sürüm, MySQL entegrasyonundan önce akış ve tasarımın oturması için hazırlanmış statik + localStorage çalışan prototiptir.</small>
    </div>
    <div>
      <small>Şehir seçimi ve kategori seçimi combobox mantığında çalışır. Kullanıcılar kendi ilanlarını “İlanlarım” alanında görür.</small>
    </div>
  </div>
</footer>
'''

files['index.html'] = f'''
<!DOCTYPE html><html lang="tr"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pazarium - İkinci El Alım Satım Platformu</title>
<link rel="stylesheet" href="css/style.css"></head><body>
{header.format(base='')}
<section class="hero">
  <div class="container">
    <div class="hero-card">
      <div class="hero-inner">
        <div class="hero-copy">
          <span class="eyebrow">⚡ Modern pazar yeri deneyimi · Sahip olduğun ürünü hızla vitrine çıkar</span>
          <h1>İkinci el alışverişi daha güvenli, daha hızlı ve daha şık hale getir.</h1>
          <p>Sahibinden benzeri akış mantığıyla tasarlanmış bu sürümde öne çıkan ilanlar, detaylı kart yapısı, güçlü ilan detay sayfası ve doğrudan fotoğraf seçerek ilan ekleme deneyimi yer alıyor.</p>
          <div class="hero-stats">
            <div class="stat-card"><div class="stat-value">8+</div><div class="stat-label">Hazır demo ilan</div></div>
            <div class="stat-card"><div class="stat-value">Yerel</div><div class="stat-label">Fotoğraf yükleme önizlemesi</div></div>
            <div class="stat-card"><div class="stat-value">Kendi</div><div class="stat-label">İlanlarını yönet</div></div>
          </div>
        </div>
        <div class="hero-panel">
          <img src="assets/images/hero-market.svg" alt="Pazar yeri vitrini">
          <h3>Ürününü birkaç adımda yayınla</h3>
          <p>Kategori ve şehir seçimi dropdown mantığında çalışır. Fotoğraf URL’i yerine doğrudan bilgisayarından görsel seçip anında önizleyebilirsin.</p>
          <div class="badges">
            <span class="badge">Fotoğraf seçerek ilan ver</span>
            <span class="badge">Benzer ilan kartları</span>
            <span class="badge">Modern detay ekranı</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container content-grid">
    <aside class="sidebar">
      <div class="sidebar-card">
        <h3>Kategoriler</h3>
        <nav class="category-list">
          <a class="active" href="pages/listings.html">Tüm İlanlar <span>›</span></a>
          {''.join(f'<a href="pages/listings.html?category={c["id"]}">{c["label"]} <span>›</span></a>' for c in [{'id':'telefon','label':'Cep Telefonu'},{'id':'bilgisayar','label':'Bilgisayar'},{'id':'vasita','label':'Vasıta'},{'id':'ev-esyasi','label':'Ev Eşyası'},{'id':'kamera','label':'Fotoğraf & Kamera'},{'id':'mobilya','label':'Mobilya'}])}
        </nav>
      </div>
    </aside>
    <main class="page-main">
      <div class="section-head">
        <div>
          <h2 class="section-title">Öne çıkan vitrin ilanları</h2>
          <p class="section-subtitle">Fiyat, kategori ve satıcı yapısı öne çıkarılmış profesyonel kart görünümü.</p>
        </div>
        <a class="outline-btn" href="pages/listings.html">Tüm ilanlara git</a>
      </div>
      <div id="featuredListings" class="grid-cards"></div>
    </main>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <div>
        <h2 class="section-title">Yeni eklenen ilanlar</h2>
        <p class="section-subtitle">Liste ve detay ekranlarında aynı profesyonel görünüm korunur.</p>
      </div>
    </div>
    <div id="latestListings" class="grid-cards"></div>
  </div>
</section>
{footer}
<script src="js/data.js"></script><script src="js/store.js"></script><script src="js/ui.js"></script><script src="js/main.js"></script>
</body></html>
'''

files['pages/listings.html'] = f'''
<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>İlanlar - Pazarium</title><link rel="stylesheet" href="../css/style.css"></head><body>
{header.format(base='../')}
<section class="page-hero"><div class="container"><div class="section-head"><div><h1 class="section-title">İlanlar</h1><p class="section-subtitle">Sahibinden benzeri yapıya yakın olarak; filtre, kart düzeni, şehir ve kategori combobox mantığı ile tasarlandı.</p></div><div class="ribbon-note" id="listingCount"></div></div></div></section>
<section class="section"><div class="container page-grid">
  <aside class="sidebar"><div class="sidebar-card"><h3>Kategori Geçişleri</h3><nav class="category-list">
    <a href="listings.html">Tüm İlanlar</a>
    <a href="listings.html?category=telefon">Cep Telefonu</a>
    <a href="listings.html?category=bilgisayar">Bilgisayar</a>
    <a href="listings.html?category=vasita">Vasıta</a>
    <a href="listings.html?category=ev-esyasi">Ev Eşyası</a>
    <a href="listings.html?category=kamera">Fotoğraf & Kamera</a>
    <a href="listings.html?category=mobilya">Mobilya</a>
  </nav></div></aside>
  <main class="page-main">
    <div class="filter-bar">
      <input id="filterQuery" type="text" placeholder="Ürün adı, marka veya model ara">
      <select id="filterCategory" data-categories data-placeholder="Kategori seç"></select>
      <select id="filterCity" data-cities data-placeholder="Şehir seç"></select>
      <select id="filterSort"><option value="newest">En Yeni</option><option value="priceAsc">Fiyat Artan</option><option value="priceDesc">Fiyat Azalan</option></select>
      <button class="outline-btn" id="clearFilters">Temizle</button>
      <div class="filter-icon">☰</div>
    </div>
    <div id="listingGrid" class="grid-cards"></div>
  </main>
</div></section>
{footer}
<script src="../js/data.js"></script><script src="../js/store.js"></script><script src="../js/ui.js"></script><script src="../js/listings.js"></script>
</body></html>
'''

files['pages/detail.html'] = f'''
<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>İlan Detayı - Pazarium</title><link rel="stylesheet" href="../css/style.css"></head><body>
{header.format(base='../')}
<section class="section" id="detailRoot"><div class="container detail-layout">
  <main class="detail-main">
    <div class="detail-card">
      <ul class="breadcrumbs" id="breadcrumbs"></ul>
      <div class="gallery-main"><img id="mainImage" src="" alt="İlan görseli"><div class="gallery-nav"><button class="gallery-btn" id="prevImage">‹</button><button class="gallery-btn" id="nextImage">›</button></div></div>
      <div class="thumb-strip" id="thumbStrip"></div>
      <div class="detail-head">
        <div>
          <h1 class="detail-title" id="detailTitle"></h1>
          <div class="meta-row"><span class="meta-pill">Detaylı vitrinde gösterim</span><span class="meta-pill">Benzer ilan önerileri</span><span class="meta-pill">Profesyonel sunum</span></div>
        </div>
        <div class="detail-price" id="detailPrice"></div>
      </div>
      <div class="spec-grid" id="specGrid"></div>
      <h3>Açıklama</h3>
      <div class="description-box" id="detailDescription"></div>
      <h3 style="margin-top:20px">Öne çıkan özellikler</h3>
      <div class="meta-row" id="featureList"></div>
    </div>
    <div class="section-head" style="margin-top:20px"><div><h2 class="section-title" style="font-size:24px">Benzer ilanlar</h2><p class="section-subtitle">Aynı kategori içinde ilgini çekebilecek diğer seçenekler.</p></div></div>
    <div id="similarGrid" class="similar-grid"></div>
  </main>
  <aside class="seller-card" id="sellerCard"></aside>
</div></section>
{footer}
<script src="../js/data.js"></script><script src="../js/store.js"></script><script src="../js/ui.js"></script><script src="../js/detail.js"></script>
</body></html>
'''

files['pages/create-listing.html'] = f'''
<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>İlan Ver - Pazarium</title><link rel="stylesheet" href="../css/style.css"></head><body>
{header.format(base='../')}
<section class="section"><div class="container"><div class="section-head"><div><h1 class="section-title">Yeni İlan Oluştur</h1><p class="section-subtitle">Şehir, kategori ve durum alanlarında combobox mantığı kullanılır. Fotoğraf URL yerine doğrudan cihazından fotoğraf seçersin.</p></div></div>
<div class="form-shell">
  <div class="surface form-card">
    <form id="listingForm" class="form-grid">
      <input class="full" id="title" type="text" placeholder="İlan başlığı" required>
      <input id="price" type="number" placeholder="Fiyat" required>
      <input id="oldPrice" type="number" placeholder="Eski fiyat (opsiyonel)">
      <select id="category" data-categories data-placeholder="Kategori seç" required></select>
      <select id="city" data-cities data-placeholder="Şehir seç" required></select>
      <input id="district" type="text" placeholder="İlçe / Semt" required>
      <input id="brand" type="text" placeholder="Marka" required>
      <input id="model" type="text" placeholder="Model" required>
      <input id="year" type="number" placeholder="Yıl" required>
      <select id="condition" required>
        <option value="">Kullanım durumu</option>
        <option>İkinci El</option><option>Sıfır Ayarında</option><option>Yeni Gibi</option>
      </select>
      <select id="status" required>
        <option value="">İlan durumu</option>
        <option>Yeni Gibi</option><option>Temiz</option><option>Bakımlı</option><option>Ekspertiz Hazır</option>
      </select>
      <input id="label" type="text" placeholder="Kart etiketi (örn: Öne Çıkan)">
      <textarea class="full" id="description" placeholder="Ürünü detaylı anlat" required></textarea>
      <input class="full" id="features" type="text" placeholder="Özellikleri virgülle yaz: 128 GB, Kutulu, Faturalı">
      <div class="full dropzone" id="dropzone">
        <strong>Fotoğrafları sürükle bırak</strong>
        <p class="hint">Ya da aşağıdaki alandan seç. En fazla 6 fotoğraf ekleyebilirsin.</p>
        <input id="images" type="file" accept="image/*" multiple>
        <div class="upload-grid" id="uploadPreview"></div>
      </div>
      <button class="primary-btn full" style="padding:16px 18px">İlanı Yayınla</button>
    </form>
  </div>
  <aside class="surface form-card">
    <h3>Bu sürümde neler hazır?</h3>
    <ul class="bullet-list hint">
      <li>• Şehir ve kategori alanları dropdown/combobox olarak ayarlı.</li>
      <li>• Seçtiğin fotoğraflar anında önizlenir.</li>
      <li>• Kaydettiğin ilan, “İlanlarım” ekranında görünür.</li>
      <li>• Oluşturduğun ilan detay sayfasında profesyonel görünür.</li>
      <li>• Sonraki adımda aynı yapıyı MySQL’e bağlayacağız.</li>
    </ul>
  </aside>
</div></div></section>
{footer}
<script src="../js/data.js"></script><script src="../js/store.js"></script><script src="../js/ui.js"></script><script src="../js/create-listing.js"></script>
</body></html>
'''

files['pages/my-listings.html'] = f'''
<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>İlanlarım - Pazarium</title><link rel="stylesheet" href="../css/style.css"></head><body>
{header.format(base='../')}
<section class="section"><div class="container">
  <div class="section-head"><div><h1 class="section-title">İlanlarım</h1><p class="section-subtitle"><span id="welcomeUser"></span> hesabına ait oluşturduğun ilanlar burada listelenir.</p></div><a class="primary-btn" href="create-listing.html">Yeni İlan Ekle</a></div>
  <div class="account-summary">
    <div class="summary-tile"><div class="hint">Toplam ilan</div><div class="value" id="myCount">0</div></div>
    <div class="summary-tile"><div class="hint">Kayıtlı şehir</div><div class="value" id="myCity">-</div></div>
    <div class="summary-tile"><div class="hint">Panel durumu</div><div class="value">Aktif</div></div>
  </div>
  <div id="myListingsGrid" class="grid-cards"></div>
</div></section>
{footer}
<script src="../js/data.js"></script><script src="../js/store.js"></script><script src="../js/ui.js"></script><script src="../js/my-listings.js"></script>
</body></html>
'''

files['pages/login.html'] = f'''
<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Giriş Yap - Pazarium</title><link rel="stylesheet" href="../css/style.css"></head><body>
{header.format(base='../')}
<section class="section"><div class="container"><div class="surface auth-card"><h1 class="section-title" style="font-size:30px">Hesabına giriş yap</h1><p class="section-subtitle">Demo kullanıcı için: demo@pazarium.com / herhangi bir şifre yerine kayıt ekranından yeni kullanıcı açman daha iyi olur.</p>
<form id="loginForm" class="form-grid" style="margin-top:16px">
<input class="full" id="loginEmail" type="email" placeholder="E-posta" required>
<input class="full" id="loginPassword" type="password" placeholder="Şifre" required>
<button class="primary-btn full" style="padding:15px 16px">Giriş Yap</button>
</form><div class="auth-switch">Hesabın yok mu? <a href="register.html" style="color:var(--blue);font-weight:700">Hemen kayıt ol</a></div></div></div></section>
{footer}
<script src="../js/data.js"></script><script src="../js/store.js"></script><script src="../js/ui.js"></script><script src="../js/auth.js"></script>
</body></html>
'''

files['pages/register.html'] = f'''
<!DOCTYPE html><html lang="tr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Kayıt Ol - Pazarium</title><link rel="stylesheet" href="../css/style.css"></head><body>
{header.format(base='../')}
<section class="section"><div class="container"><div class="surface auth-card"><h1 class="section-title" style="font-size:30px">Yeni hesap oluştur</h1><p class="section-subtitle">Bu aşamada hesaplar tarayıcıda localStorage ile tutulur. Sonraki turda aynısını MySQL tabanlı gerçek sisteme taşıyacağız.</p>
<form id="registerForm" class="form-grid" style="margin-top:16px">
<input id="fullName" type="text" placeholder="Ad Soyad" required>
<input id="phone" type="text" placeholder="Telefon" required>
<input class="full" id="registerEmail" type="email" placeholder="E-posta" required>
<select id="city" data-cities data-placeholder="Şehir seç" required></select>
<input id="registerPassword" type="password" placeholder="Şifre" required>
<div></div>
<button class="primary-btn full" style="padding:15px 16px">Hesap Oluştur</button>
</form><div class="auth-switch">Zaten hesabın var mı? <a href="login.html" style="color:var(--blue);font-weight:700">Giriş yap</a></div></div></div></section>
{footer}
<script src="../js/data.js"></script><script src="../js/store.js"></script><script src="../js/ui.js"></script><script src="../js/auth.js"></script>
</body></html>
'''

files['README.txt'] = '''
PAZARIUM - FRONTEND FIRST PROTOTYPE

Bu sürümde hazır olanlar:
- modern ve animasyonlu tasarım
- şehir ve kategori combobox/select mantığı
- demo statik ilan verileri
- ilan listeleme sayfası
- profesyonel ilan detay sayfası
- benzer ilanlar alanı
- kullanıcı kayıt / giriş akışı (localStorage)
- ilan ekleme formu
- URL yerine direkt fotoğraf seçme ve önizleme
- kullanıcının kendi oluşturduğu ilanları görebildiği “İlanlarım” sayfası

NASIL AÇILIR?
1) frontend klasörünü VS Code ile aç.
2) index.html dosyasını Live Server ile çalıştır.
3) İstersen önce register ekranından yeni kullanıcı aç.
4) create-listing ekranından fotoğraf seçip yeni ilan oluştur.
5) my-listings ekranında kendi ilanlarını gör.

NOT:
Bu aşamada veri tabanı yok. Bilgiler tarayıcının localStorage alanında tutulur.
Sonraki adımda aynı yapıyı MySQL + backend API ile bağlamak çok daha kolay olacaktır.
'''

# create SVG images
svg_templates = {
'hero-market.svg': ('Pazarium Vitrin', '#ffd400', '#2f6fed', 'Ürününü kolayca sat'),
'phone-1.svg': ('iPhone 14 Pro', '#4f46e5', '#111827', 'Telefon'),
'phone-2.svg': ('Face ID / 128 GB', '#2f6fed', '#1f2937', 'Kutu Faturalı'),
'phone-3.svg': ('Pil Sağlığı %89', '#ffd400', '#3b82f6', 'Temiz Kullanım'),
'laptop-1.svg': ('MacBook Air M2', '#0f172a', '#60a5fa', 'Laptop'),
'laptop-2.svg': ('Retina Display', '#1d4ed8', '#93c5fd', '8/256'),
'laptop-3.svg': ('Az Kullanıldı', '#334155', '#cbd5e1', 'Kusursuz Gövde'),
'car-1.svg': ('VW Golf', '#f59e0b', '#111827', 'Boyasız'),
'car-2.svg': ('DSG / Life', '#2563eb', '#0f172a', 'Servis Bakımlı'),
'car-3.svg': ('79.000 km', '#1d4ed8', '#f8fafc', 'Masrafsız'),
'sofa-1.svg': ('L Koltuk', '#a855f7', '#fdf4ff', 'Mobilya'),
'sofa-2.svg': ('Yıkanabilir Kumaş', '#f472b6', '#fff1f2', 'Temiz'),
'sofa-3.svg': ('Modern Salon', '#fb7185', '#ffe4e6', 'Az Kullanıldı'),
'camera-1.svg': ('Sony A7 III', '#111827', '#f59e0b', 'Kamera'),
'camera-2.svg': ('Full Frame', '#0f172a', '#38bdf8', 'Lens Dahil'),
'camera-3.svg': ('4K Video', '#1d4ed8', '#f8fafc', 'Düşük Shutter'),
'console-1.svg': ('PS5 Slim', '#1d4ed8', '#0f172a', '2 Kol'),
'console-2.svg': ('FIFA 25', '#2563eb', '#111827', 'Kutulu'),
'console-3.svg': ('Temiz Konsol', '#334155', '#f8fafc', 'Sorunsuz'),
'bike-1.svg': ('Elektrikli Bisiklet', '#16a34a', '#0f172a', '45 km'),
'bike-2.svg': ('Katlanır Gövde', '#0f766e', '#f0fdfa', 'Şehir İçi'),
'bike-3.svg': ('Batarya İyi', '#059669', '#ecfdf5', 'Bakımlı'),
'tv-1.svg': ('Samsung 55"', '#1d4ed8', '#111827', '4K UHD'),
'tv-2.svg': ('Smart TV', '#0f172a', '#60a5fa', 'Wi‑Fi'),
'tv-3.svg': ('Kumandalı', '#334155', '#f8fafc', 'Çiziksiz'),
}

def svg_text(title, c1, c2, sub):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800">
  <defs>
    <linearGradient id="g" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="800" rx="40" fill="url(#g)"/>
  <circle cx="980" cy="120" r="120" fill="rgba(255,255,255,.18)"/>
  <circle cx="220" cy="680" r="160" fill="rgba(255,255,255,.12)"/>
  <rect x="130" y="170" width="940" height="460" rx="34" fill="rgba(255,255,255,.12)" stroke="rgba(255,255,255,.22)"/>
  <text x="160" y="310" fill="white" font-size="72" font-family="Arial" font-weight="800">{title}</text>
  <text x="160" y="380" fill="rgba(255,255,255,.84)" font-size="34" font-family="Arial">{sub}</text>
  <text x="160" y="560" fill="rgba(255,255,255,.82)" font-size="26" font-family="Arial">Pazarium demo görseli</text>
</svg>'''

for rel, content in files.items():
    path = base / rel if not rel.startswith('README') else Path('/mnt/data/marketpro') / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).strip(), encoding='utf-8')

for name, args in svg_templates.items():
    (base / 'assets/images' / name).write_text(svg_text(*args), encoding='utf-8')

