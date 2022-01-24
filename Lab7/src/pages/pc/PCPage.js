import {PCComponent} from "../../components/pc/PCComponent.js";
import {MainPage} from "../main/MainPage.js";
import {BackButtonComponent} from "../../components/back-button/BackButtonComponent.js";
import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";

export class PCPage {
    constructor(parent, id) {
        this.parent = parent
        this.id = id
    }

    async getData() {
        return ajax.get(urls.pc(this.id))
    }

    get page() {
        return document.getElementById('pc-page')
    }

    getHTML() {
        return (
            `
                <div id="pc-page">
                </div>
            `
        )
    }

    clickBack() {
        const mainPage = new MainPage(this.parent)
        mainPage.render()
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const backButton = new BackButtonComponent(this.page)
        backButton.render(this.clickBack.bind(this))

        const data = await this.getData()
        const pc = new PCComponent(this.page)
        pc.render(data.data)
    }
}