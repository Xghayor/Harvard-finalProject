document.querySelector("#myForm button").addEventListener("click", function () {
    var x = $("form").serializeArray();
    $.each(x, function (i, field) {
      var place = field.value;
  
      const apiKey = "500d8896c9f22504fa8586dea352e7f1";
  
      const url =
        "https://api.openweathermap.org/data/2.5/weather?q=" +
        place +
        " &units=metric&appid=" +
        apiKey +
        "";
  
      async function fetching(url) {
        const response = await fetch(url);
        var weatherData = await response.json();
  
        const desc = weatherData.weather[0].description;
        const temp = weatherData.main.temp;
        const icon = weatherData.weather[0].icon;
        const humidity = weatherData.main.humidity;
        const speed = weatherData.wind.speed;
  
        let imageUrl = "http://openweathermap.org/img/wn/" + icon + "@2x.png ";
        let images = "https://source.unsplash.com/1600x900/?landscape";
  
        $("#weather")
          .addClass("weather-upd")
          .html("Weather in " + place);
        $("#temp")
          .html(+temp + "<span>&#8451;</span>")
          .addClass("temp-upd ");
        $("#images2")
          .addClass("  clouds-upd ")
          .html("<img  src=" + imageUrl + "/>" + desc);
        $("#humidity")
          .html("Humidity  : " + humidity)
          .addClass("humidity-upd");
        $("#windspeed")
          .html("Wind speed : " + speed)
          .addClass("windspeed-upd");
        let d = new Date();
        $("#bg-img").attr("src", images + "?" + d.getTime());
      }
  
      fetching(url);
    });
  });


  const loader = document.querySelector('.loader');
  const bgImage = document.getElementById('bg-img');

  // Show the loader while the image is being fetched
  bgImage.addEventListener('load', () => {
    loader.style.display = 'none';
  });

  // Hide the loader when there's an error loading the image
  bgImage.addEventListener('error', () => {
    loader.style.display = 'none';
  });

  // Function to handle button click
  function handleButtonClick() {
    // Show the loader when the button is clicked
    loader.style.display = 'block';
    // Implement your logic for handling the button click here
  }

  // Attach the button click event listener
  const button = document.querySelector('.pressed');
  button.addEventListener('click', handleButtonClick);