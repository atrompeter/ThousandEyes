fetch('https://api.thousandeyes.com/v6/alerts.json', {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${47ee7d76-4783-40f6-b574-0b2c80e68ea4}`
  }
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error(error));
