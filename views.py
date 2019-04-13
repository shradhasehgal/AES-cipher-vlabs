from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def introduction():
	return render_template('Introduction.html', topic ='Introduction')

@app.route("/experiment")
def experiment():
	return render_template('Experiment.html', topic ='Experiment')

@app.route("/manual")
def manual():
	return render_template('Manual.html', topic ='Manual')

@app.route("/theory")
def theory():
	return render_template('Theory.html', topic ='Theory')

@app.route("/objective")
def objective():
	return render_template('Objective.html', topic ='Objective')

@app.route("/quiz")
def quiz():
	return render_template('Quizzes.html', topic ='Quiz')

@app.route("/feedback")
def feedback():
	return render_template('Feedback.html', topic ='Feedback')

@app.route("/procedure")
def procedure():
	return render_template('Procedure.html', topic ='Procedure')

@app.route("/further")
def further():
	return render_template('Further.html', topic ='Further Readings')


if __name__ == '__main__':
	app.run(debug = True)