function nextPlainText() {
    $.ajax({
type: "GET",
url:"/experiment/nextplaintext",

success: function(result){
$('#plainarea').text(result.plainarea);
console.log(result);
console.log(result.plainarea)

var iv = $("#ivtext");
		var ctr = $("#ctrtext");

		iv.hide();
		ctr.hide();

		$("select#mode").change(function() {
			iv.show();
			ctr.show();

			if (this.value == "ecb") {
				iv.hide();
				ctr.hide();
			} else if (this.value == "cbc") {
				ctr.hide();
			} else if (this.value == "ctr") {
				iv.hide();
			} else if (this.value == "ofb") {
				ctr.hide();
			}
		});
}
});
}

function nextKey() {
    $.ajax({
type: "GET",
url:"/experiment/nextkey",


success: function(result){
$('#keyarea').text(result.key);
console.log(result.key)
}
});
}

function nextIV() {
    $.ajax({
type: "GET",
url:"/experiment/nextIV",


success: function(result){
$('#iv').text(result.iv);
}
});
}

function nextCtr() {
    $.ajax({
type: "GET",
url:"/experiment/nextctr",


success: function(result){
$('#ctr').text(result.ctr);
//console.log(result);
console.log("Ctr printed")
console.log(result.ctr)
}
});
}
