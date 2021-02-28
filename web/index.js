const date = document.querySelector("#date");
const progress = document.querySelector("#encodeProgress");
const image = document.querySelector("#cameraRenderer");
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
function loadCSVFile(filePath) {
  // change csv file address here
  d3.text(filePath, function (data) {
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
  eel.image_loader();
});

// will fire if `encode` button's click action triggered
encodeButton.addEventListener("click", function () {
  // runs eel's encoder function
  eel.encoder();
});

// will fire if `save` button's click action triggered
saveButton.addEventListener("click", function () {
  // runs eel's save_encodings function
  eel.save();
});

// will fire if `start` button's click action triggered to display csv file as a table
startButton.addEventListener("click", function () {
  // runs eel's recognizer function
  eel.recognizer()();
});

eel.expose(updateImageSrc);
function updateImageSrc(val) {
  image.src = "data:image/jpeg;base64," + val;
}

// will fire if `stop` button's click action triggered to remove video src
stopButton.addEventListener("click", function () {
  image.src = "./images/blank.png";
  // eel.stop();
});
