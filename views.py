from flask import Flask, render_template, jsonify, request
from reqIss import *
from appy import *

app = Flask(__name__)

## Having a default object when no object is selected
aes_obj = aesMeth()

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


@app.route("/experiment/selectMode", methods=['POST'])
def selectMode():
    data = request.get_json()
    Mode = str(data.get)
    print(Mode)

@app.route("/experiment/selectKey", methods=['POST'])
def selectKey():
    data = request.get_json()
    keySize = str(data.get)

@app.route("/experiment/nextplaintext", methods=['GET'])
def nextplaintext():
    aes_obj.genPlainText()

    info = {
                "plainarea": aes_obj.printPt()
    }

    return jsonify(info)


@app.route("/experiment/nextkey", methods=['GET'])
def nextkey():
        aes_obj.genKey()

        info = {
            "key": aes_obj.printKey()
        }

        return jsonify(info)

@app.route("/experiment/nextIV", methods=['GET'])
def nextIV():
        aes_obj.genIV()

        info = {
            "iv": aes_obj.printIV()
        }

        return jsonify(info)

@app.route("/experiment/nextctr", methods=['GET'])
def nextctr():
    aes_obj.genCtr()

    info = {
        "ctr": aes_obj.printCtr()
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
