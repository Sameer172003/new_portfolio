from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)
app.secret_key = "my_secret_key" 

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/project')
def project():
    return render_template("project.html")

@app.route('/certificate')
def certificate():
    return render_template("certificate.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        with open('submissions.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message])

        return redirect('/contact') 
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
