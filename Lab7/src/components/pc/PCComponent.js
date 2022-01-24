export class PCComponent {
    constructor(parent) {
        this.parent = parent
    }

    getHTML(data) {
        return (
            `
                <div class="card mb-3" style="width: 540px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="https://cdn-icons-png.flaticon.com/512/1941/1941784.png" class="img-fluid" alt="картинка">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">${data.name}</h5>
                                <p class="card-subtitle">Операционная система:</p>
                                <p class="card-text">${data.op_system}</p>
                                <p class="card-subtitle">Объем оперативной памяти:</p>
                                <p class="card-text">${data.ram_storage} GB</p>
                            </div>
                        </div>
                    </div>
                </div>
            `
        )
    }

    render(data) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
    }
}