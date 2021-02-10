const date = document.querySelector("#date");
const progress = document.querySelector("#encodeProgress");
const video = document.querySelector("#videoElement");
const startButton = document.querySelector("#start");
const stopButton = document.querySelector("#stop");
const statistics = document.querySelector(".statistics");

// change date value
const dateOptions = {
  weekday: "long",
  year: "numeric",
  month: "long",
  day: "numeric",
};
date.textContent = new Date().toLocaleDateString("en-US", dateOptions);

// change progress bar value
progress.value = 80;

// webcam access grant
if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
      video.load();
      video.play();
    })
    .catch(function (error) {
      console.log("Something went wrong!");
      console.error(error);
    });
}

// will fire if `start` button's click action triggered to display csv file as a table
startButton.addEventListener("click", function () {
  if (statistics.innerHTML === "") {
    // change csv file address
    d3.text("addresses.csv", function (data) {
      const parsedCSV = d3.csv.parseRows(data);

      d3.select(".statistics")
        .append("table")
        .selectAll("tr")
        .data(parsedCSV)
        .enter()
        .append("tr")
        .selectAll("td")
        .data(function (d) {
          return d;
        })
        .enter()
        .append("td")
        .text(function (d) {
          return d;
        });
    });
  }
});

// will fire if `stop` button's click action triggered to remove video src
stopButton.addEventListener("click", function () {
  video.srcObject = "";
});
