document.getElementsByTagName("button")[0].addEventListener("click", function(event) {
    event.preventDefault();
    weight = document.getElementById("weight").value;
    height = document.getElementById("height").value;
    bmi = weight / (height * height);
    document.getElementById("result").innerText = "Your BMI is " + bmi.toFixed(4);
});