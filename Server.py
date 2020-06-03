from flask import Flask, render_template
import random
app = Flask(__name__)

number_of_questions = 8

@app.route('/')
def M1():
	rand = random.randint(1, 2)
	if rand == 1:
		print("User given money version")
		return render_template("M1.html")
	else:
		print("User given points version")
		return render_template("P1.html")

@app.route('/<type>/<number>/<answer>')
def serve(type, number, answer):
	assert type in ["P", "M"]
	assert int(number) <= (number_of_questions + 1)
	assert int(number) > 0
	assert answer in ["A", "B"]
	filename = "./results/" + str(type) + str(int(number) - 1) + ".txt"
	print("Writing answer", answer, "to", filename)
	file = open(filename, "a")
	datum = str(answer) + "\n"
	file.write(datum)
	file.close()
	if int(number) == (number_of_questions + 1):
		return "done :)"
	page = str(type) + str(number) + ".html"
	print("Serving page", page)
	return render_template(page)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8084)
