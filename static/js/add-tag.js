
const options = document.getElementsByName('item-tag')
var inputListTag = document.getElementById('id_tags')
const container = document.getElementById('row-tags')
const buttons = document.getElementsByName('btn-alert-tag')

var cont = 0
var itemsSelected = []


function setClickClose(value) {
    const index = itemsSelected.indexOf(value)
    itemsSelected.splice(index - 1, index + 1)

    inputListTag.value = itemsSelected
    cont -= 1
}

for (let i = 0; i < options.length; i++) {
    options[i].addEventListener('click', () => {
        checkItem(options[i].textContent)
    })
}

const checkItem = (itemName) => {
    if (cont < 4 && itemsSelected.indexOf(itemName) == -1) {
        itemsSelected.push(itemName)
        const tag = new Tag(itemName)
        container.appendChild(tag.getElemet())
        
        inputListTag.value = itemsSelected
        cont += 1
    }
}


class Tag {

    constructor(value){
        this.descrip = value
        this.alertTag = document.createElement('div')
        this.title = document.createElement('strong')
        this.button = document.createElement('button')
        this.span = document.createElement('span')

        this.setAtributeElement()
        this.putElementChild()
    }

    setAtributeElement() {
        this.alertTag.setAttribute("role", "alert")
        this.alertTag.setAttribute('class', 'alert alert-warning alert-dismissible fade show ml-4')
    
        this.title.innerText = `#${this.descrip}`
    
        this.button.setAttribute('class', 'close')
        this.button.setAttribute('type', 'button')
        this.button.setAttribute('data-dismiss', 'alert')
        this.button.setAttribute('aria-label', 'Close')
        this.button.setAttribute('name', 'btn-alert-tag')
        this.button.setAttribute('onClick', `setClickClose("${this.descrip}")`)
    
        this.span.setAttribute('aria-hidden', 'true')
        this.span.innerHTML = '&times;'
    }

    putElementChild() {
        this.button.appendChild(this.span)
        this.alertTag.appendChild(this.title)
        this.alertTag.appendChild(this.button)
    }

    getElemet() {
        return this.alertTag
    }
}



