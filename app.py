from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("base_wizytowka.html")

@app.route('/me')
def me():
    return render_template("Moja_wizytowka.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("Moja_wizytowka_2.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")

