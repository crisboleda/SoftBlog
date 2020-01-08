

var inputListTag = document.getElementById('id_tags')
var choices = inputListTag.value.split(',')
itemsSelected = choices

for (let j = 0; j < choices.length; j++) {
    const tag = new Tag(choices[j])
    container.appendChild(tag.getElemet())

    inputListTag.value = itemsSelected
    cont += 1
}


