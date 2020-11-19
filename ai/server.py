from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("trails.html");


@app.route('/profile')
def user_profile():
    return render_template("user_page.html");


if __name__ == "__main__":
    app.run();