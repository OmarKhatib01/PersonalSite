from flask import Flask, render_template

jinjavar= Flask(__name__)
@jinjavar.route('/<food>/<book>')
def pickFood(food, book):
	return render_template("jinjavar.html", food=food, book= book)

if __name__ == "__main__":
	jinjavar.run(port=5000)