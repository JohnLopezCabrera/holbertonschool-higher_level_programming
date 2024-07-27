document.addEventListener('DOMContentLoaded', function() {
    const redHeaderDiv = document.getElementById('red_header');
    const header = document.querySelector('header');
    
    redHeaderDiv.addEventListener('click', function() {
      header.classList.add('red');
    });
  });
