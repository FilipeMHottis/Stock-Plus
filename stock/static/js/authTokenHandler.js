import Token from './class/token.js';
import getTokenStorage from './utils/getTokenStorage.js';

const verifyAndRefreshToken = async () => {
    const storageInstance = getTokenStorage();

    if (!storageInstance) {
        window.location.href = '/login/';
        return;
    }

    const accessToken = storageInstance.get('access_token');
    const refreshToken = storageInstance.get('refresh_token');
    const token = new Token(accessToken, refreshToken);

    try {
        const data = await token.verifyAccessToken();
        if (!data) {
            const refreshedData = await token.updateToken();
            if (refreshedData && refreshedData.access_token && refreshedData.refresh_token) {
                storageInstance.set('access_token', refreshedData.access_token);
                storageInstance.set('refresh_token', refreshedData.refresh_token);
            } else {
                window.location.href = '/login/';
            }
        }
    } catch (error) {
        console.error('Erro ao verificar ou atualizar o token:', error);
        window.location.href = '/login/';
    }
}

setInterval(verifyAndRefreshToken, 60000);
verifyAndRefreshToken();

export default getTokenStorage;
