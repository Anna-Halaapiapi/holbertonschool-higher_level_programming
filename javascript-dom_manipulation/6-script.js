// fetches char name from: https://swapi-api.hbtn.io/api/people/5/?format=json. Display name in the HTML tag with id 'character'
async function getdata () { // promise based func
  const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json'); // fetch data, waits until fin
  const data = await response.json(); // converts response obj to usable json data, waits until fin
  const name = data.name; // gets name from json data
  document.getElementById('character').textContent = name; // updates name in the HTML tag with id character
}
getdata();
