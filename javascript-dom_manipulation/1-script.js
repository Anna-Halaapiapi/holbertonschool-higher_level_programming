const h = document.getElementById("red_header"); // select element with 'red_header' ID
h.addEventListener("click", color_change); // add click event listener to red_header element
function color_change() { //function to change color of header to red
  document.querySelector("header").style.color = "#FF0000";
}
