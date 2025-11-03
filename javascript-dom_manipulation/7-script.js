// fetches and lists the title for all movies from: https://swapi-api.hbtn.io/api/films/?format=json
async function getdata () { // promise based func
  const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json'); // fetch data
  const data = await response.json(); // conv to json
  const list = document.getElementById('list_movies'); // get 'list_movies' ul

  for (const movie of data.results) { // loop through results list
    const item = document.createElement('li'); // create new li item
    item.textContent = movie.title; // add title to new li item
    list.appendChild(item); // add li to ul
  }
}
getdata();
