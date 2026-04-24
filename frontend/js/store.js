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