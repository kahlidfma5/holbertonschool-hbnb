/* 
  This is a SAMPLE FILE to get you started.
  Please, follow the project instructions to complete the tasks.
*/
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
    return document.cookie.substring(cindex+name.length+1);
}
async function fetchPlaces(token){
const url="http://127.0.0.1:5000/api/v1/places";
try{
  const response = await fetch(url,{
    headers:{
      "Authorization":"Bearer "+token,
      "Content-Type": "application/json",
          "Accept": "application/json"
    }
  
    });
    if(!response.ok){
      throw new Error(`Response status: ${response.status}`);
      }
    res = await response.json();
    console.log(res);
    }
    catch(error){
      console.log(error.message);
    }
}
document.addEventListener('DOMContentLoaded', () => {
  const login_form = document.getElementById('login-form');
  if(!login_form)
    checkAuthentication();

  login_form.addEventListener('submit', async (event) => {
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
      window.location = "index.html"
    } catch (error) {
      console.error(error.message);
    }
  });

  
});