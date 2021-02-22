const date = document.querySelector("#date");
const progress = document.querySelector("#encodeProgress");
const video = document.querySelector("#videoElement");
const loadButton = document.querySelector("#load");
const encodeButton = document.querySelector("#encode");
const saveButton = document.querySelector("#save");
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
date.textContent = new persianDate().format("dddd, DD MMMM YYYY");

// will change progress bar value
function updateProgress(value) {
  progress.value = value;
}

// will load svg file
function loadCSVFile() {
  // change csv file address here
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

// will fire if `load` button's click action triggered
loadButton.addEventListener("click", function () {
  // runs eel's image_loader function
  console.log("`load` button clicked!"); // remove this line
  eel.image_loader();
});

// will fire if `encode` button's click action triggered
encodeButton.addEventListener("click", function () {
  // runs eel's encoder function
  console.log("`encode` button clicked!"); // remove this line
  eel.encoder();
});

// will fire if `save` button's click action triggered
saveButton.addEventListener("click", function () {
  // runs eel's save_encodings function
  console.log("`save` button clicked!"); // remove this line
  eel.save_encodings();
});

// will fire if `start` button's click action triggered to display csv file as a table
startButton.addEventListener("click", function () {
  console.log("`start` button clicked!"); // remove this line
  if (statistics.innerHTML === "") {
    // runs eel's recognizer function
    eel.recognizer().then(function () {
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

      // runs eel's csv_reader function
      eel.csv_reader().then(function () {
        loadCSVFile();
      });
    });
  }
});

// will fire if `stop` button's click action triggered to remove video src
stopButton.addEventListener("click", function () {
  console.log("`stop` button clicked!"); // remove this line
  const mediaStream = video.srcObject;
  const tracks = mediaStream.getTracks();
  tracks.forEach((track) => track.stop());
  video.src = "";
});
