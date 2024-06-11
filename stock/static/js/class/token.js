class Token {
    constructor(token, refresh) {
        this.accessToken = token;
        this.refreshToken = refresh;
    }

    getAccessToken() {
        return this.accessToken;
    }

    getRefreshToken() {
        return this.refreshToken;
    }

    setAccessToken(token) {
        this.accessToken = token;
    }

    setRefreshToken(refresh) {
        this.refreshToken = refresh;
    }

    clearTokens() {
        this.accessToken = null;
        this.refreshToken = null;
    }

    async verifyAccessToken() {
        try {
            const response = await fetch('/auth/token/verify/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    token: this.accessToken,
                }),
            });

            if (response.ok) {
                const data = await response.json();
                return data; // Ou alguma lógica para lidar com a verificação
            } else {
                throw new Error('Token de acesso inválido');
            }
        } catch (error) {
            console.error('Erro ao verificar o token:', error);
            return null;
        }
    }

    async updateToken() {
        try {
            const response = await fetch('/auth/token/refresh/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    refresh: this.refreshToken,
                }),
            });

            if (response.ok) {
                const data = await response.json();
                this.setAccessToken(data.access);
                if (data.refresh) {
                    this.setRefreshToken(data.refresh);
                }
                return data;
            } else {
                throw new Error('Não foi possível atualizar o token');
            }
        } catch (error) {
            console.error('Erro ao atualizar o token:', error);
            return null;
        }
    }
}

export default Token;
