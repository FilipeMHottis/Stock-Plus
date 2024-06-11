import getTokenStorage from './utils/getTokenStorage.js';
import Category from './class/category.js';

const form = document.querySelector('form');
const name = document.querySelector('#id_name');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const storage = getTokenStorage();

    if (!storage) {
        window.location.href = '/login/';
        return;
    }

    const token = storage.get('access_token');
    const category = new Category(name.value, token);

    try {
        await category.add_category();
        window.alert('Categoria criada com sucesso!');
    } catch (error) {
        console.error('Erro ao criar a categoria:', error);
    }
});
