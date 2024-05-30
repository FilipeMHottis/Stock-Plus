class Storage {
    constructor(sessionOrLocal) {
        if (sessionOrLocal === 'session') {
            this.storage = sessionStorage;
        } else {
            this.storage = localStorage;
        }
    }

    get(key) {
        return this.storage.getItem(key);
    }

    set(key, value) {
        this.storage.setItem(key, value);
    }

    remove(key) {
        this.storage.removeItem(key);
    }

    clear() {
        this.storage.clear();
    }

    getKeys() {
        return Object.keys(this.storage);
    }

    getValues() {
        return Object.values(this.storage);
    }

    getEntries() {
        return Object.entries(this.storage);
    }

    getLength() {
        return this.storage.length;
    }
}

export default Storage;
