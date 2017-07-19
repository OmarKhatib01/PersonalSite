from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def home1(): 
    return render_template("home.html", title= "Omar Khatib-Home")
@app.route('/home.html')
def home(): 
    return render_template("home.html", title= "Omar Khatib-Home")
@app.route('/about.html')
def about():
	return render_template("about.html", title= "Omar Khatib-About")
@app.route('/Articles.html')
def work():
	return render_template("Articles.html", title= "Omar Khatib-My Work")

@app.route("/test.html")
def listExample():
	text = ["Ahmad", "Mahmoud", "Hamdy", "Hamdan", "Hamood"]
	display= True
	return render_template("test.html",display=display, list=text )

if __name__ == "__main__":
	app.run(port=3000)