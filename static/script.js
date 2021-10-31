// let app = document.getElementById("app");
// let h1 = document.createElement('h1');
// h1.innerText = 'From javascript';
// app.prepend(h1);

var imgInput = document.getElementById("imgInput")
var imgOutput = document.getElementById("imgOutput")
changeScale = () => {
    document.getElementById("inputPercentage").innerHTML = document.getElementById("inputScale").value
    document.getElementById("pixelDiff").innerHTML = document.getElementById("inputScale").value
}
showImgInput = (event) => { // referensi: https://stackoverflow.com/a/27165977
    imgInput = document.getElementById("imgInput")
    imgInput.src = URL.createObjectURL(event.target.files[0])
    imgInput.onload = () => {
        URL.revokeObjectURL(imgInput.src)
    }
    showImgOutput(event)
}
// TODO: connect backend di sini
showImgOutput = (event) => {
    imgOutput = document.getElementById("imgOutput");
    imgOutput.src = URL.createObjectURL(event.target.files[0])
    imgOutput.onload = () => {
        URL.revokeObjectURL(imgOutput.src)
    }
}

var imgOutput = document.getElementById("imgOutput")
imgOutput.addEventListener("mouseenter", () => {
    imgOutput.style.filter += "brightness(150%)"
})
imgOutput.addEventListener("mouseleave", () => {
    imgOutput.style.removeProperty("filter")
})