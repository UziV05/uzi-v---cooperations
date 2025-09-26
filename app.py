from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():  # Make sure function is named 'home'
    return render_template("index.html")

# About page
@app.route('/about')
def about():
    return render_template("about.html")

# Services page
@app.route('/services')
def services():
    return render_template("services.html")

# Contact page
@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
