from flask import Flask, render_template, request, jsonify, redirect
import random
app = Flask(__name__)

number_of_questions = 8

def IPcompletedQuestion(filename, ip):
    f = open(filename, "r")
    contents = str(f.read())
    f.close()
    return ip in contents

@app.route("/paper")
def servePaper():
    return redirect("https://docs.google.com/document/d/1xDDLbEQb2pLG5VQAK6Xhr8eFaq1RKqCCtLUbqS9hRss/edit?usp=sharing")

@app.route('/HackMainframe')
def easterEgg():
    return "You're in"

@app.route('/end')
def debrief():
    return render_template("end.html")

@app.route('/')
def index():
    rand = random.randint(1, 2)
    if rand == 1:
        print("User given money version")
        return render_template("Mstart.html")
    else:
        print("User given points version")
        return render_template("Pstart.html")

@app.route('/<version>/<number>/<answer>', methods=["GET"])
def serve(version, number, answer):
    assert version in ["P", "M"]
    assert int(number) <= (number_of_questions + 1)
    assert int(number) > 0
    assert answer in ["A", "B", "X"]
    if answer is not "X":
        #ip_addr = str(jsonify({'ip': request.remote_addr}))
        ip_addr = str(request.headers.getlist("X-Forwarded-For")[0])
        ip_file = "./ip/" + str(int(number) - 1) + "ip.txt"
        repeat_user = IPcompletedQuestion(ip_file, ip_addr)
        if not repeat_user:
            filename = "./results/" + str(version) + str(int(number) - 1) + ".txt"
            print("Writing answer", answer, "to", filename)
            file = open(filename, "a")
            datum = str(answer) + "\n"
            file.write(datum)
            file.close()
            ipfile = open(ip_file, "a")
            print("adding ip", ip_addr)
            ipfile.write(ip_addr + "\n")
            ipfile.close()
    if int(number) == (number_of_questions + 1):
        return render_template("end.html")
    page = str(version) + str(number) + ".html"
    print("Serving page", page)
    return render_template(page)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8084)
