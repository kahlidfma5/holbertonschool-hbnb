/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
  console.log(queryString(window.location.href).id);
  if (document.getElementById('price-filter'))
    document.getElementById('price-filter').addEventListener('change', (event) => {
      // Get the selected price value
      places = document.getElementById("places-list").children;
      for (place of places) {
        if (document.getElementById("price-filter").value == "All" ||
          place.children[1].innerHTML === document.getElementById("price-filter").value) {

          place.style.display = "block";
        }
        else if (place.children[1].innerHTML !== document.getElementById("price-filter").value) {
          place.style.display = "none";
        }
      }
    });
  console.log("Loading");
  if (!(document.getElementById('login-form'))) {
    console.log("No Login");

    checkAuthentication();
  }
  if (document.getElementById('login-form')) {
    document.getElementById('login-form').addEventListener('submit', async (event) => {
      event.preventDefault(); // Prevents the browser from navigating to example.com
      const url = "http://127.0.0.1:5000/api/v1/auth/login";

      try {
        const response = await fetch(url, {
          method: "POST",
          body: JSON.stringify({ email: document.getElementById("email").value, password: document.getElementById("password").value }),
          headers: {
            "Content-Type": "application/json",
            "Accept": "application/json"
          },
        });
        if (!response.ok) {
          throw new Error(`Response status: ${response.status}`);
        }

        const json = await response.json();
        console.log(json['access_token']);

        document.cookie = "token=" + json['access_token'];
        document.cookie = 'id='+json['id'];
        console.log("I am redirecting");
        window.location = "index.html"
      } catch (error) {
        console.error(error.message);
      }
    });

  }
  if (document.getElementById('review-form')) {
    document.getElementById('review-form').addEventListener('submit', async (event) => {
      event.preventDefault(); // Prevents the browser from navigating to example.com
      const url = "http://127.0.0.1:5000/api/v1/reviews/";
      const token = getCookie('token');
      if (token) {
        try {
          const response = await fetch(url, {
            method: "POST",
            body: JSON.stringify({
              text: document.getElementById("review-text").value,
              rating: parseFloat(document.getElementById("rating").value),
              user_id: getCookie('id'),
              place_id: queryString(window.location.href).id
            }),
            headers: {
              "Content-Type": "application/json",
              "Authorization": "Bearer " + getCookie('token'),
              "Accept": "application/json"
            },
          });
          if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
          }

          window.location.reload();
        } catch (error) {
          console.error(error.message);
        }
      }


    });

  }
});

function checkAuthentication() {
  const token = getCookie("token");

  console.log(token);

  if (!token) {
    if (document.getElementById('login-link'))
      document.getElementById('login-link').style.display = 'block';
    if (document.getElementById('add-review'))
      document.getElementById('add-review').style.display = 'none';
  } else {
    if (document.getElementById('login-link'))
      document.getElementById('login-link').style.display = 'none';
    if (document.getElementById('add-review'))
      document.getElementById('add-review').style.display = 'block';
    // Fetch places data if the user is authenticated
    if (document.getElementById('places-list'))
      fetchPlaces(token);
    if (document.getElementById('place-details'))
      fetchPlaceDetails(token, queryString(window.location.href).id);
  }
  return token;
}
function getCookie(name) {
  let cookieArr = document.cookie.split(";");
    
    // Loop through the array elements
    for(let i = 0; i < cookieArr.length; i++) {
        let cookiePair = cookieArr[i].split("=");
        
        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if(name == cookiePair[0].trim()) {
            // Decode the cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }
    
    // Return null if not found
    return null;
}

async function fetchPlaces(token) {
  const url = "http://127.0.0.1:5000/api/v1/places/";
  try {
    const response = await fetch(url, {
      headers: {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Accept": "application/json"
      }

    });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    res = await response.json();
    displayPlaces(res);
    console.log(res);
  }
  catch (error) {
    console.log(error.message);
  }
}

async function fetchPlaceDetails(token, placeId) {
 // console.log("ID=" + placeId);
  // Make a GET request to fetch place details
  // Include the token in the Authorization header
  // Handle the response and pass the data to displayPlaceDetails function
  const url = "http://127.0.0.1:5000/api/v1/places/" + placeId;
  try {
    const response = await fetch(url, {
      headers: {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Accept": "application/json"
      }

    });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    res = await response.json();
    displayPlaceDetails(res);
  }
  catch (error) {
    console.log(error.message);
  }
}
function displayPlaceDetails(place) {
  console.log(place);
  document.getElementById('place-name').innerHTML = place.title;
  document.getElementById('place-host').innerHTML = "<b>Host: </b>"+place.user_name;
  document.getElementById('place-price').innerHTML = "<b>Price Per Night: $</b>"+place.price;
  document.getElementById('place-description').innerHTML = "<b>Description: </b>"+place.description;

  document.getElementById("reviews-list").innerHTML = "";
  html_reviews = document.getElementById("reviews-list")
  // Iterate over the places data
  // For each place, create a div element and set its content
  // Append the created element to the places list

  place.reviews.forEach(element => {
    review_ul = document.createElement("ul");
    html_reviews.appendChild(review_ul);

    review_li = document.createElement('li');
    review_ul.appendChild(review_li);

    review_user = document.createElement("b");
    review_user.innerHTML = element.user_name + ":";
    review_li.appendChild(review_user);

    review_text = document.createElement("p");
    review_text.innerHTML = element.text;
    review_li.appendChild(review_text);

    review_rating = document.createElement("p");
    review_rating.innerHTML = "<b>Rating: </b> "+element.rating;
    review_li.appendChild(review_rating);
    //review_li.innerHTML = review_li.innerHTML + element.rating;

  });

  // Clear the current content of the place details section
  // Create elements to display the place details (name, description, price, amenities and reviews)
  // Append the created elements to the place details section
}
function queryString(url) {
  console.log(url);
  const query = url.split('?')[1];
  const params = {};

  if (query) {
    const pairs = query.split('&');
    for (const pair of pairs) {
      const [key, value] = pair.split('=');
      params[key] = decodeURIComponent(value
        .replace(/\+/g, ' '));
    }
  }

  return params;
}
function displayPlaces(places) {
  // Clear the current content of the places list
  document.getElementById("places-list").innerHTML = "";
  html_places = document.getElementById("places-list")
  // Iterate over the places data
  // For each place, create a div element and set its content
  // Append the created element to the places list
  places.forEach(element => {
    place_card = document.createElement("div");
    place_card.classList.add("place-card");
    html_places.appendChild(place_card);

    place_title = document.createElement("h3");
    place_title.innerHTML = element.title;
    place_card.appendChild(place_title);

    place_price = document.createElement("p");
    place_price.innerHTML = 'Price per night: $'+element.price;
    place_card.appendChild(place_price);

    place_link = document.createElement("a");
    place_link.innerHTML = "View Details";
    place_link.href = "place.html?id=" + element.id;
    place_card.appendChild(place_link);

  });
}