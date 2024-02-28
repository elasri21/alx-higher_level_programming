$(document).ready(function () {
  const btn = $('#add_item');
  const listItems = $('UL.my_list');
  btn.click(function () {
    listItems.append('<li>Item</li>');
  });
});
