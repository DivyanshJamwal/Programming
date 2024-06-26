const URL = "https://makemytrip-backend-w2d2.onrender.com/cities";

const cityContainer = document.querySelector('.city_container')
const searchInput = document.querySelector('#search-input');

let cityData = []
let timeoutId = null;

const data = fetch(URL)

data.then((res)=>{
    return res.json()
}).then((data)=>{
    data.forEach(createCard)
    const searchCities = throttle((searchTerm) => {
        cityContainer.innerHTML = '';
        const filteredCities = cityData.filter((city) => {
          return city.city.toLowerCase().includes(searchTerm.toLowerCase());
        });
        if (filteredCities.length === 0) {
          const noResultsMessage = document.createElement('p');
          noResultsMessage.textContent = 'No cities found';
          cityContainer.appendChild(noResultsMessage);
        } else {
          filteredCities.forEach(createCard);
        }
      }, 500);
  
      searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value;
        searchCities(searchTerm);
      });
    });


const createCard = (cityData, index)=>{
    const {id, city, description, image} = cityData
    const card = document.createElement("div")
    card.className = "card"
    card.addEventListener

    const cardImage = document.createElement("img")
    cardImage.src = image
    cardImage.alt = city

    const cityInfo = document.createElement("div")
    cityInfo.className = "city-info"

    const cityName = document.createElement("h3")
    cityName.className = "city-name"
    cityName.textContent = city

    const cityDescription = document.createElement("p")
    cityDescription.className = "city-description"
    cityDescription.textContent = description

    cityInfo.appendChild(cityName)
    cityInfo.appendChild(cityDescription)

    card.appendChild(cardImage)
    card.appendChild(cityInfo)

    cityContainer.appendChild(card)
}

const throttle = (func, wait) => {
    let timeoutId = null;
    return function(...args) {
      if (timeoutId) {
        clearTimeout(timeoutId);
      }
      timeoutId = setTimeout(() => {
        func(...args);
      }, wait);
    };
  };
  
//   const searchCities = throttle((searchTerm) => {
//     console.log('cityData:', cityData);
//     console.log('searchTerm:', searchTerm);
//     cityContainer.innerHTML = '';
//     const filteredCities = cityData.filter((city) => {
//       return city.city.toLowerCase().includes(searchTerm.toLowerCase());
//     });
//     if (filteredCities.length === 0) {
//       const noResultsMessage = document.createElement('p');
//       noResultsMessage.textContent = 'No cities found';
//       cityContainer.appendChild(noResultsMessage);
//     } else {
//       filteredCities.forEach(createCard);
//     }
//   }, 500);
  
  
//   searchInput.addEventListener('input', (e) => {
//     const searchTerm = e.target.value;
//     searchCities(searchTerm);
//   });