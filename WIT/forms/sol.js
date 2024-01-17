document.getElementById('registrationForm').onsubmit = function(event) {
    event.preventDefault();
    var username = document.getElementById('username').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    if(username && email && password) {
      console.log('Form submitted:', username, email, password);
    } else {
      alert('Please fill out all fields.');
    }
  };