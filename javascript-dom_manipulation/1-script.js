// updates the text color of the header element to red (#FF0000) when the user clicks on the tag with id red_header
const h = document.getElementById('red_header'); // select element with 'red_header' ID
h.addEventListener('click', colorchange); // add click event listener to red_header element
function colorchange () { // function to change color of header to red
  document.querySelector('header').style.color = '#FF0000';
}
