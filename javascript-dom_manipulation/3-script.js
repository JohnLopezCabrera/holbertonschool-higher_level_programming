document.addEventListener('DOMContentLoaded', function() {
    const toggleHeaderDiv = document.getElementById('toggle_header');
    const header = document.querySelector('header');

    toggleHeaderDiv.addEventListener('click', function() {

      if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
      } else {
        header.classList.remove('green');
        header.classList.add('red');
      }
    });
  });
