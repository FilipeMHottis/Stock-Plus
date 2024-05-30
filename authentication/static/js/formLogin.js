import Storage from "./storage.js";

const formLogin = document.querySelector('form');

formLogin.addEventListener('submit', function (event) {
    event.preventDefault();

    const username = document.querySelector('input[name="username"]').value;
    const password = document.querySelector('input[name="password"]').value;
    const rememberMeCheckbox = document.querySelector('input[name="remember_me"]');
    const sessionOrLocal = rememberMeCheckbox.checked ? 'local' : 'session';

    var storage = new Storage(sessionOrLocal);

    fetch('/auth/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({username, password}),
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Usuário ou senha inválidos');
        }
    }).then(data => {
        storage.set('access_token', data.access);
        storage.set('refresh_token', data.refresh);
    }).catch(error => {
        alert(error.message);
    });

    formLogin.reset();
    document.querySelector('input[name="username"]').focus();
});
