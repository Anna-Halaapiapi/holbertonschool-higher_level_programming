// adds a li element to a list when the user clicks on the element with id add_item
const el = document.getElementById('add_item'); // select el with id add_item
el.addEventListener('click', addLi); // add event listenter
function addLi () { // function to add li to ul
  const list = document.querySelector('.my_list'); // get ul el with class my_list
  const item = document.createElement('li'); // create new li item
  item.textContent = 'Item'; // add text to new li item
  list.appendChild(item); // add li item to ul el
}
