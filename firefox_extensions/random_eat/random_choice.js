//class="header-wrap l-container"
//console.log(document.body.children)
let doc = document.getElementsByClassName("menuCard-wrapper")

//drikkevarer på https://www.just-eat.dk/restaurants-golden-pizza/menu
let category = doc[0]['firstElementChild']['children'][0]['innerText']

let subCategory = doc[0]['firstElementChild']['children'][1]['childNodes'][1]['firstChild']['nextSibling']['innerText']

let itemsOfCategory = doc[0]['firstElementChild']['children'][1]['childNodes']//[1]['innerText']


function getCategoriesContent(ioc) {
	for (var i = 1; i < itemsOfCategory.length; i++) {
		let d = itemsOfCategory[i]['childNodes']
		for (var j = 0; j < d.length; j++) {
			if (d[j]['className'] == "product-synonym" ){
				console.log(d[j]['innerText'])
			}
		}
	}
}
//console.log(itemsOfCategory)
console.log("heey")



/*

let d = doc[0]['firstElementChild']['children'][1]['childNodes']

for i in d.length
	for j in d[i]['childNodes']
		d[i]['childNodes'][j]



function getCategoriesContent(ioc) {
	let items = ;
	for (var i = Things.length - 1; i >= 0; i--) {
		Things[i]
	}
}
*/
//class="header header--fixed u-horizontalRuleBottom"