console.log('jestem w js script')
var button_on = document.getElementById('btn_on');
var text_field = document.getElementById('tag');
    	
button_on.addEventListener("click", function(){
    var ourRequest = new XMLHttpRequest();
	ourRequest.open('GET','/process');
	ourRequest.onload = function() {
		var data = JSON.parse(ourRequest.responseText);
		console.log(ourRequest.responseText);
		render(data.signal);
	};
	ourRequest.send();
});

var button_off = document.getElementById('btn_off');    	
button_off.addEventListener("click", function(){
    var ourRequest = new XMLHttpRequest();
	ourRequest.open('GET','/process2');
	ourRequest.onload = function() {				
		var data = JSON.parse(ourRequest.responseText);
		console.log(ourRequest.responseText);
		render(data.signal);
	};
	ourRequest.send();
});
function render(data){
    text_field.innerHTML = 'status: ' + data;
};