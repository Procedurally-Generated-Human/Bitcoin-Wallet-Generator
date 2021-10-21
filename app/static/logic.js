var input = document.getElementById("salt");
var inputValue = document.getElementById("salt").value;


input.addEventListener("keypress", function() {
    inputValue = document.getElementById("salt").value;
    if (input.value.length <= 50) {
        document.getElementById('guide').innerHTML = "Please Enter More Than 50 Characters";
    }
    else if (input.value.length <= 80){
        document.getElementById('guide').innerHTML = "Enter More Than 80 Characters For Better Security";
    
    }

});

