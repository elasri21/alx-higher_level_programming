document.addEventListener('DOMContentLoaded', function () {
  $(document).ready(function () {
    const myList = $('UL.my_list');
    const addItem = $('DIV#add_item');
    const removeItem = $('DIV#remove_item');
    const clearList = $('DIV#clear_list');
    addItem.click(function () {
      myList.append('<li>Item</li>');
    });
    removeItem.click(function () {
      $('UL.my_list li:last-child').remove();
    });
    clearList.click(function () {
      myList.empty();
    });
  });
});
