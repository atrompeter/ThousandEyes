fetch('https://api.thousandeyes.com/v6/alerts.json', {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${api_token}`
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error));
