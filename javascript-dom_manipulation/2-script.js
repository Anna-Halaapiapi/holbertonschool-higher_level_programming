const h = document.getElementById('red_header'); // select element with 'red_header' ID
h.addEventListener('click', addclass); // add click event listener to red_header element
function addclass () { // function to add class red to header element
  document.querySelector('header').classList.add('red');
}
