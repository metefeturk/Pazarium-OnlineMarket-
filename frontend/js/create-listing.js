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