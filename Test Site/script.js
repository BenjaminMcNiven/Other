$(document).ready(function(){
    $('#myForm').submit(function(e) {
      e.preventDefault(); // Prevents the form from submitting the default way
      var selectedValue = $('#mySelect').val();
      console.log(selectedValue);  // Print the selected value to the console
    });
  });