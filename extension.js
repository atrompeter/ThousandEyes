var xhr = new XMLHttpRequest();

// Replace with your actual API token
var api_token = "YOUR_API_TOKEN";

// Base URL for the ThousandEyes API
var base_url = "https://api.thousandeyes.com";

// Endpoint for creating alerts
var endpoint = "/v6/alerts.json";

xhr.open("GET", base_url + endpoint);
xhr.setRequestHeader("Accept", "application/json");
xhr.setRequestHeader("Content-Type", "application/json");
xhr.setRequestHeader("Authorization", "Bearer " + api_token);

xhr.onload = function() {
    if (xhr.status === 200) {
        var alerts = JSON.parse(xhr.responseText);
        console.log(alerts);
    } else {
        console.error(xhr.responseText);
    }
}

xhr.send();
