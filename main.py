from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contacts():
    return render_template("contact.html")

@app.route("/about")
def abouts():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)