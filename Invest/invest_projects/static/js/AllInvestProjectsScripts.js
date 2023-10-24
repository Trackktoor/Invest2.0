function GetAllProjectsAJAX() {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://127.0.0.1:8000/ajax/get_all_projects/", true);

    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest");

    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = xhr.responseText;
            var response = JSON.parse(response);
            console.log(response)
            if (response != undefined){
                let container = document.getElementsByClassName('container_items')[0]
                for (let i = 0; i < response.length; i++){
                    let new_item = CloneTemplateItemHTML(response[i])
                    container.appendChild(new_item)
                }
            }
        }
    };

    xhr.send();
}

function CloneTemplateItemHTML(item_info) {
    let itemTempalte = document.getElementById('item_template')
    let item_clone = document.importNode(itemTempalte.content, true)

    let item_container = item_clone.children[0]

    item_container.querySelector('.item_image').src = item_info['images_urls'][0]
    item_container.querySelector('.info_title').textContent = item_info['title']
    item_container.querySelector('.item_image_a').href = '/project/'+ String(item_info['id'])

    item_container.querySelector('.metric_profitability--info').textContent = item_info['profit_per_month']

    if (item_info['required_investment'] > 999999 && item_info['required_investment'] < 99999999){
        console.log(typeof(item_info['required_investment']))
        item_info['required_investment'] = String(item_info['required_investment']).slice(0,-6) + 'млн'
    }

    item_container.querySelector('.metric_attachments--info').textContent = item_info['required_investment']

    return item_clone
}

GetAllProjectsAJAX()