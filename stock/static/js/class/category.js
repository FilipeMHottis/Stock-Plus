class Category {
    constructor(name, token) {
        this.id = null;
        this.name = name;
        this.token = token;
    }

    get category() {
        return {
            id: this.id,
            name: this.name
        };
    }

    set category(category) {
        this.id = category.id;
        this.name = category.name;
    }

    async add_category() {
        const response = await fetch('/api/categories/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.token}`
            },
            body: JSON.stringify({ name: this.name })
        });
        // this.category = await response.json();
        return await response.json();
    }

    async update_category() {
        const response = await fetch(`/api/categories/${this.id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${this.token}`
            },
            body: JSON.stringify(this.category)
        });
        // this.category = await response.json();
        return await response.json();
    }

    async delete_category() {
        await fetch(`/api/categories/${this.id}/`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        });
    }

    static async get_categories() {
        const response = await fetch('/api/categories/');
        return await response.json();
    }

    static async get_category(id) {
        const response = await fetch(`/api/categories/${id}/`);
        return await response.json();
    }

    static async get_category_products(id) {
        const response = await fetch(`/api/categories/${id}/products/`);
        return await response.json();
    }
}

export default Category;
