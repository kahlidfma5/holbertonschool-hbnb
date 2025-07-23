/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/

document.addEventListener('DOMContentLoaded', () => {
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
        console.log("I am redirecting");
        window.location = "index.html"
      } catch (error) {
        console.error(error.message);
      }
    });

  }
});

function checkAuthentication() {
  const token = getCookie("token");
  const loginLink = document.getElementById('login-link');
  console.log(token);

  if (!token) {
    loginLink.style.display = 'block';
  } else {
    loginLink.style.display = 'none';
    // Fetch places data if the user is authenticated
    fetchPlaces(token);
  }
}
function getCookie(name) {
  cindex = document.cookie.indexOf(name);
  console.log(cindex);
  return document.cookie.substring(cindex + name.length + 1);
}
function getPlaces() {
  console.log("PLACES");
}

async function fetchPlaces(token) {
  console.log("I am called");
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

    place_title = document.createElement("b");
    place_title.innerHTML = element.title;
    place_card.appendChild(place_title);

    place_price = document.createElement("p");
    place_price.innerHTML = element.price;
    place_card.appendChild(place_price);

    place_link = document.createElement("a");
    place_link.innerHTML = "View Details";
    place_link.href = "/place/" + element.id;
    place_card.appendChild(place_link);

  });
}