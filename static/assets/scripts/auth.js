(function () {
    'use strict';

    const AUTH_KEY = 'hroom_auth';
    const USER_KEY = 'hroom_user';
    const LOGIN_KEY = 'hroom_login';

    const isAuthorized = () => localStorage.getItem(AUTH_KEY) === 'true';

    function clearSession() {
        localStorage.removeItem(AUTH_KEY);
        localStorage.removeItem(USER_KEY);
        localStorage.removeItem(LOGIN_KEY);
    }

    function protectPage() {
        if (document.body.dataset.protected === 'true' && !isAuthorized()) {
            window.location.href = '/login/';
        }
    }

    function renderFooterAccount() {
        const box = document.getElementById('footerAccount');
        if (!box) return;

        const auth = isAuthorized();

        if (auth) {
            box.innerHTML = `
                <a href="/profile/" class="footer-link">Профиль</a>
                <a href="#" class="footer-link" id="footerLogout">Выйти</a>
            `;
            const logoutBtn = document.getElementById('footerLogout');
            if (logoutBtn) {
                logoutBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    if (confirm('Выйти из аккаунта?')) {
                        clearSession();
                        window.location.href = '/';
                    }
                });
            }
        } else {
            box.innerHTML = `
                <a href="/login/" class="footer-link">Войти</a>
                <a href="/register/" class="footer-link">Регистрация</a>
            `;
        }
    }

    document.addEventListener('DOMContentLoaded', () => {
        protectPage();
        renderFooterAccount();
    });
})();