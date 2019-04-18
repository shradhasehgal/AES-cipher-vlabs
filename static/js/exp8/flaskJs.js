function nextPlainText() {
    $.ajax({
		type: "GET",
		url:"/experiment/nextplaintext",

		success: function(result){
			$('#plainarea').text(result.plainarea);
			console.log(result);
			console.log(result.plainarea)
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
		console.log("Ctr printed")
		console.log(result.ctr)
		}
	});
}

/*function checkQuiz() {
    $.ajax({
		type: "GET",
		url:"/experiment/quizdata",

	success: function(result){
		c = 0
		var str=""
		if(result["one"] == "1")
		{
			c+=1
			str+="Answer 1: Correct\n"
		}

		if(result["two"] == "ECB")
		{
			c+=1
			str += "Answer 2: Correct\n"
		}

		if(result["three"] == "1")
		{
			c+=1
			str += "Answer 3: Correct\n"
		}

		alert("You scored "+c+"/3"+'\n'+str)
	});
}
}*/
