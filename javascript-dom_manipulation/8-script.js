// fetch:  https://hellosalut.stefanbohacek.com/?lang=fr, display value of hello in HTML element with id hello
document.addEventListener('DOMContentLoaded', async function () { // waits until DOM fully loaded
  const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr'); // fetch data
  const data = await response.json(); // conv to json

  const el = document.getElementById('hello'); // get HTML el with id hello
  el.textContent = data.hello; // update text in el
});
