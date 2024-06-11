import Storage from '../class/storage.js';


const getTokenStorage = () => {
    const localToken = new Storage('local');
    const sessionToken = new Storage('session');

    return localToken || sessionToken;
};

export default getTokenStorage;
