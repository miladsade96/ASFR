const date = document.querySelector("#date");
const progress = document.querySelector("#encodeProgress");
const video = document.querySelector("#videoElement");

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
