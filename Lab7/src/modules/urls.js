class Urls {
    constructor() {
        this.url = 'http://127.0.0.1:8000/';
    }

    pcs() {
        return `${this.url}PC/`
    }

    pc(id) {
        return `${this.url}PC/${id}/`
    }
}

export const urls = new Urls()