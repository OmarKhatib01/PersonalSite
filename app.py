from flask import Flask, render_template, request
import dataset
db = dataset.connect("postgres://xsjzjpzyhkoidq:c4bcbe9bee44314992f147122e2364f148ec630b0c629da67d96a9ab80b81ccb@ec2-23-21-96-159.compute-1.amazonaws.com:5432/d5u1piikmon387")
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
	return render_template("test.html",display=display , list=text )

@app.route("/contactme.html", methods=["GET", "POST"])
def contactMe():
	if request.method == "GET":
		return render_template("contactme.html")
	else:
		form = request.form
		if request.method == "POST":
			name = form["Name"]
			email = form["Email"]
			message = form["Message"]
			contactsTable = db["contacts"]
			entry = {"name":name, "email":email, "message":message}
			contactsTable.insert(entry)
			return render_template("contactmedata.html", Name = name, Email = email, Message= message )

@app.route("/contactmedata")
def showContact():
	form = request.form
	name = form["Name"]
	email = form["Email"]
	message = form["Message"]
	contactsTable = db["contacts"]
	entry = {"name":name, "email":email, "message":message}
	contactsTable.insert(entry)
	print list(contactsTable.all())
	return render_template ("contactmedata.html", Name = name, Email = email, Message= message)

@app.route("/showAll")
def showAll():
	contacts = db["contacts"]
	allContacts = list(contacts.all())
	return render_template ("showAll.html", contacts=allContacts)

if __name__ == "__main__":
	app.run(port=3000)