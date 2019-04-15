from flask import Flask, render_template, jsonify, request
from reqIss import *
from Crypto.Cipher import AES

app = Flask(__name__)

## Having a default object when no object is selected
aes_obj = aesMeth()
key = 128

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
    if data == 'ecb':
        aes_obj.mode = 'ECB'
    elif data == 'cbc':
        aes_obj.mode = 'CBC'
    elif data == 'ofb':
        aes_obj.mode = 'OFB'
    elif data == 'ctr':
        aes_obj.mode = 'CTR'

@app.route("/experiment/selectKey", methods=['POST'])
def selectKey():
    data = request.get_json()
    if data == "128":
        aes_obj.keySize = 128
        key = 128
    elif data == '192':
        aes_obj.keySize = 192
        key = 192
    elif data == '256':
        aes_obj.keySize = 256
        key = 256
    else:
        print("WTF")

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

    #If the text has some spaces it wont be taken into consideration
    oneEdit = one.split(" ")
    one = ""
    for i in oneEdit:
        one+=i
    twoEdit = two.split(" ")
    two = ""
    for i in twoEdit:
        two+=i

    xor_value = printReadable(xor(one,two),8)
    print(xor_value)
    return jsonify(xor_value)

@app.route("/experiment/encrypt", methods=['GET','POST'])
def encrypt():
    data = request.get_json()
    one = str(data.get('one'))
    two = str(data.get('two'))

    #If the text has some spaces it wont be taken into consideration
    oneEdit = one.split(" ")
    one = ""
    for i in oneEdit:
        one+=i
    twoEdit = two.split(" ")
    two = ""
    for i in twoEdit:
        two+=i

    aes_new = AES.new(bytes.fromhex(one),AES.MODE_ECB)
    enc = aes_new.encrypt(bytes.fromhex(two))
    ans = printReadable(enc.hex(),8)
    return jsonify(ans)

@app.route("/experiment/decrypt", methods=['GET','POST'])
def decrypt():
    data = request.get_json()
    one = str(data.get('one'))
    two = str(data.get('two'))

    #If the text has some spaces it wont be taken into consideration
    oneEdit = one.split(" ")
    one = ""
    for i in oneEdit:
        one+=i
    twoEdit = two.split(" ")
    two = ""
    for i in twoEdit:
        two+=i

    aes_new = AES.new(bytes.fromhex(one),AES.MODE_ECB)
    dec = aes_new.decrypt(bytes.fromhex(two))
    ans = printReadable(dec.hex(),8)
    return jsonify(ans)

@app.route("/experiment/check", methods=['GET','POST'])
def checkAns():
    one = request.get_json()

    #If the text has some spaces it wont be taken into consideration
    oneEdit = one.split(" ")
    one = ""
    for i in oneEdit:
        one+=i

    if one == aes_obj.encrypt().hex():
        ret = "True"
    else:
        ret = "False"
    return jsonify(ret)


if __name__ == '__main__':
    app.run(debug = True)
