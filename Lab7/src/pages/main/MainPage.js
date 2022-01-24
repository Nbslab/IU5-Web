import {PCPage} from "../pc/PCPage.js";
import {PCCardComponent} from "../../components/pc-card/PCCardComponent.js";
import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";

export class MainPage{
    constructor(parent) {
        this.parent = parent;
    }
    async getData() {
        return ajax.get(urls.pcs())
    }

    get page() {
        return document.getElementById('main-page')
    }

    getHTML() {
        return (
            `
            <div id="main-page" class="d-flex flex-wrap"><div/>
        `
        )
    }


    clickCard(e) {
        const cardId = e.target.dataset.id
        const pcPage = new PCPage(this.parent, cardId)
        pcPage.render()
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const data = await this.getData()
        data.data.forEach((item) => {
            const pcCard = new PCCardComponent(this.page)
            pcCard.render(item, this.clickCard.bind(this))
        })
    }
}

