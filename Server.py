from flask import Flask, render_template
import random
app = Flask(__name__)

number_of_questions = 8

@app.route('/HackMainframe')
def easterEgg():
	return "You're in"

@app.route('/end')
def debrief():
	return return_template("end.html")

@app.route('/')
def index():
	rand = random.randint(1, 2)
	if rand == 1:
		print("User given money version")
		return render_template("Mstart.html")
	else:
		print("User given points version")
		return render_template("Pstart.html")

@app.route('/<version>/<number>/<answer>')
def serve(version, number, answer):
	assert version in ["P", "M"]
	assert int(number) <= (number_of_questions + 1)
	assert int(number) > 0
	assert answer in ["A", "B", "X"]
	if answer is not "X":
		filename = "./results/" + str(version) + str(int(number) - 1) + ".txt"
		print("Writing answer", answer, "to", filename)
		file = open(filename, "a")
		datum = str(answer) + "\n"
		file.write(datum)
		file.close()
	if int(number) == (number_of_questions + 1):
		return render_template("end.html")
	page = str(version) + str(number) + ".html"
	print("Serving page", page)
	return render_template(page)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8084)
