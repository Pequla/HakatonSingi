try{
var video = document.querySelector('#video');
const socket = new WebSocket('ws://localhost:6000');
const fps = 15;

if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function (stream) {
		console.log("Video input");
      video.srcObject = stream;
    })
    .catch(function (err0r) {
      console.log("Something went wrong");
    });
	
	console.log("Pozicija 1");
	
    const getFrame = () => {
            const canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0);
            const data = canvas.toDataURL('image/png');
            return data;
	}
	
	console.log("Pozicija 2");
	socket.open = () => {
		console.log("Connected to websocket")
		setInterval(() => {
			socket.send(getFrame());
		}, 1000/fps);
	}
}
console.log("Izvan");
} catch (error){
	console.log(error)
}