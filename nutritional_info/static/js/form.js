
/*Open form controll*/

// Avoid double selection in male and female checkbox selection
document.addEventListener("DOMContentLoaded", function() {
  const checkboxes = document.querySelectorAll(".btn-check");
  
  checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener("change", function() {
      if (this.checked) {
        checkboxes.forEach(function(otherCheckbox) {
          if (otherCheckbox !== checkbox) {
            otherCheckbox.checked = false;
          }
        });
      }
    });
  });
});

//Controll input lenght
document.addEventListener("DOMContentLoaded", function(){
    var fieldinput = document.querySelectorAll(".form-control");

    fieldinput.forEach(function(input){
        input.addEventListener("input", function(){
            if (input.value.length > 3) {
                input.value = input.value.slice(0, 3);
            } 
        })
    })
    
})

//Make gender checkboxes mandactory
document.getElementById("form-class").addEventListener("submit", function(event){
  function gender_checkbox() {
    const female_box = document.getElementById('female')
    const male_box = document.getElementById('male')
  
    if (female_box.checked || male_box.checked) {
      return true
    }
  
    else {
      console.log("gender checkbox validation has failed")
      event.preventDefault();
    }
  };

  function activity_form(){
    var list_form = document.getElementById('list_form');
    if (list_form.value != "0") {
      return true
    }

    else {
      console.log("activity list validation has failed")
      event.preventDefault();
    }
  };


  if (gender_checkbox() && activity_form()) {
    return 
  }

  else {
    alert('Selecione todos os campos por favor');
    console.log("functions validation has failed");
    event.preventDefault();
  }
}


);
/*Close form controll*/


  




