from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template("index.html")

# About page
@app.route('/about')
def about():
    return render_template("about.html")

# Services page
@app.route('/services')
def services():
    return render_template("services.html")

# Blog page
@app.route('/blog')
def blog():
    return render_template("blog.html")

# Careers page
@app.route('/careers')
def careers():
    return render_template("careers.html")

# Contact page
@app.route('/contact')
def contact():
    return render_template("contact.html")

# Portfolio page
@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")

# Solutions page
@app.route('/solutions')
def solutions():
    return render_template("solutions.html")

if __name__ == "__main__":
    app.run(debug=True)
