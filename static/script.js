// let app = document.getElementById("app");
// let h1 = document.createElement('h1');
// h1.innerText = 'From javascript';
// app.prepend(h1);

var imgInput = document.getElementById("imgInput")
var imgOutput = document.getElementById("imgOutput")

changeScale = () => {
    document.getElementById("inputPercentage").innerHTML = document.getElementById("inputScale").value
}

showImgInput = (event) => { // referensi: https://stackoverflow.com/a/27165977
    imgInput.src = URL.createObjectURL(event.target.files[0])
    imgOutput.remove
    imgInput.onload = () => {
        URL.revokeObjectURL(imgInput.src)
    }
    showImgOutput(event)
}

showImgOutput = (event) => {
    imgOutput.src = URL.createObjectURL(event.target.files[0])
    imgOutput.onload = () => {
        URL.revokeObjectURL(imgOutput.src)
    }
}

displayLoading = () => {
    
    document.getElementById("loading").classList.remove("d-none")
    document.getElementById("result").classList.add("d-none")
}

var imgOutput = document.getElementById("imgOutput")
imgOutput.addEventListener("mouseenter", () => {
    document.getElementById("downloadButton").classList.remove("d-none")
})
imgOutput.addEventListener("mouseleave", () => {
    document.getElementById("downloadButton").classList.add("d-none")
})