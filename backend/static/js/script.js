function encodeImageFileAsURL(element){
    alert("clicked");
	var file = element.files[0];
	var reader = new FileReader();
	var loader = "/static/images/loader.gif";
    reader.onloadend = function() {  
        var imagebase64 = reader.result;  
        $("#original").attr('src', imagebase64);
        $.post("http://127.0.0.1:8000/model/", JSON.stringify({"img": imagebase64}), function(response){
            console.log(response.model_path);
        })
    }  
    reader.readAsDataURL(file);
}

function resultButton(){

    $("#status").text("Status: working");
}

$(document).ready(function(){
    $("#original").attr('src', base64);
    var fileupload = $("#fileUpload");
    var button = $("#btnFileUpload");
    button.bind("click", function () {
        fileupload.click();
    });

});