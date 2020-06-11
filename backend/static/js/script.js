function encodeImageFileAsURL(element){

	var file = element.files[0];
	var reader = new FileReader();
	var loader = "/static/images/loader.gif";
    reader.onloadend = function() {  
        var imagebase64 = reader.result;  
        console.log(imagebase64);
        $("#original").attr('src', imagebase64);
        // $("#age-detect").attr('src', loader);
        // $("#colourise").attr('src', loader);
        // $.post("http://localhost:8000/age/", JSON.stringify({"img": imagebase64}), function(response){
        //     var ageB64 = "data:image/jpeg;base64," + response.img;
        //     $("#age-detect").attr('src', ageB64);
        //     $("#colourise").attr('src', imagebase64);
        //})
    }  
    reader.readAsDataURL(file);
}

$(document).ready(function(){
    $("#original").attr('src', base64);
    var fileupload = $("#fileUpload");
    var button = $("#btnFileUpload");
    button.bind("click", function () {
        fileupload.click();
    });    
});