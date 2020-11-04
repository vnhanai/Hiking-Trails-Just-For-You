from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("user_page.html");

@app.route('/trails')
def trails():
    return render_template("trails.html");

if __name__ == "__main__":
    app.run();