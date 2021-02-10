var video = document.querySelector("#videoElement");

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
