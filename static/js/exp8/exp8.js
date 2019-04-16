function checkQuiz() {

	c = 0
	if(document.getElementById('A1').value == "1") {
		$('#A1').css("background-color", "green");
		c+=1;
	}

	else
	{
		$('#A1').css("background-color", "red");		
	}

	if(document.getElementById('A2').value=="ECB") {
		$('#A2').css("background-color", "green");
		c+=1;
	}

	else
	{
		$('#A2').css("background-color", "red");		
	}

	if(document.getElementById('A3').value=="2"){
		$('#A3').css("background-color", "green");
		c+=1;
	}

	else
	{
		$('#A3').css("background-color", "red");		
	}

	alert("Subjective answers coming soon. You scored "+c+"/3. Congrats!");
	c=0;

}
