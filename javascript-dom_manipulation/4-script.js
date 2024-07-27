document.addEventListener('DOMContentLoaded', function() {
    const addItemDiv = document.getElementById('add_item');
    const myList = document.querySelector('.my_list');

    addItemDiv.addEventListener('click', function() {
      const newListItem = document.createElement('li');
      newListItem.textContent = 'Item';
      myList.appendChild(newListItem); // Appends the new 'li' to the 'ul' element
    });
  });
