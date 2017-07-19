from flask import Flask, render_template
import random

Quote1="damn"
Quote2="hell yeas"
Quote3="im the man"
Quote4="You're the man!!"
Quote5="Stay positive!"
app = Flask(__name__)

@app.route('/randomQuote')

def main():
    Quotes= [Quote1, Quote2,Quote3, Quote4, Quote5]
    return random.choice(Quotes)
app.run()