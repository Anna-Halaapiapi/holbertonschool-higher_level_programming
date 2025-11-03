// toggles the class of the header element when the user clicks on the tag id toggle_header
const el = document.getElementById('toggle_header'); // select element with id toggle_header
el.addEventListener('click', togglecolour); // add event listenter
function togglecolour () { // toggle class between red/green for header
  const h = document.querySelector('header');
  h.classList.toggle('red');
  h.classList.toggle('green');
}
