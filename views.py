from flask import Flask, render_template, jsonify, request
from appy import *

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

@app.route("/experiment/nextplaintext", methods=['GET'])
def nextplaintext():
	info = {
		"plainarea": rando()
	}

	return jsonify(info)


@app.route("/experiment/nextkey", methods=['GET'])
def nextkey():
	info = {
		"key": rando()
	}

	return jsonify(info)
	
@app.route("/experiment/answer", methods=['GET','POST'])
def answer():
	data = request.get_json()
	one = str(data.get('one'))
	two = str(data.get('two'))
	return jsonify(one+two)


if __name__ == '__main__':
	app.run(debug = True)
