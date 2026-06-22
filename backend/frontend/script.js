async function generateCaption(){

    const file =
    document.getElementById("imageInput").files[0];

    if(!file){
        alert("Select an image");
        return;
    }

    document.getElementById("preview").src =
    URL.createObjectURL(file);

    let formData = new FormData();

    formData.append("image", file);

    const response = await fetch(
        "http://127.0.0.1:5000/caption",
        {
            method:"POST",
            body:formData
        }
    );

    const data = await response.json();

    document.getElementById("caption").innerText =
    "Caption: " + data.caption;
}
