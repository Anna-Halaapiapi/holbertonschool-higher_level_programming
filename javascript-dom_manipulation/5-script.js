// updates the text of the header element to New Header!!! when the user clicks on the element with id update_header
const el = document.getElementById('update_header'); // select el with id update_header
el.addEventListener('click', updateText); // add event listener
function updateText () {
  const h = document.querySelector('header'); // select header
  h.textContent = 'New Header!!!'; // update text of header
}
