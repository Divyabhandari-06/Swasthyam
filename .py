from flask import Flask, render_template, request

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    weight = request.form["weight"]
    height = request.form["height"]
    return f"Weight: {weight}kg, Height: {height}cm"

if _name_ == "_main_":
    app.run(debug=True)
