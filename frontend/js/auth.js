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