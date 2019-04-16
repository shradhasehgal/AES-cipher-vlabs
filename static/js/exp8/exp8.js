function checkQuiz() {

	c = 0
	if($("#q11").is(':checked')) {
		$('#Q1').css("background-color", "green");
		c+=1;
	}

	else
	{
		$('#Q1').css("background-color", "red");		
	}

	if($("#q21").is(':checked')) {
		$('#Q2').css("background-color", "green");
		c+=1;
	}

	else
	{
		$('#Q2').css("background-color", "red");		
	}

	if($("#q31").is(':checked')){
		$('#Q3').css("background-color", "green");
		c+=1;
	}

	else
	{
		$('#Q3').css("background-color", "red");		
	}

	alert("Subjective answers coming soon. You scored "+c+"/3. Congrats!");
	c=0;

}