from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/SignUp')
def signup():
    return render_template("SignUp.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)