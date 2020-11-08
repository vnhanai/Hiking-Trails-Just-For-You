from flask import Flask
from flask import render_template, request

from user import User, AgeVerifier, CompletionVerifier, LevelRecommender

app = Flask(__name__)


@app.route("/")
def index():
    return "<button> Index! </button>"


@app.route("/user_profile", methods=['POST', 'GET'])
def user_profile():
    if request.method == 'GET':
        return render_template("user_page.html")

    if request.method == 'POST':
        profile = request.form
        age = profile.get('age')
        if age is not None:
            age = int(age)
        height = profile.get('height')
        if height is not None:
            height = float(height)
        weight = profile.get('weight')
        if weight is not None:
            weight = float(weight)
        scale = profile.get('scale')
        if scale is not None:
            scale = int(scale)
        general_health = profile.get('health')
        talk_test = profile.get('talk')
        activity_level = profile.get('activity')
        hiking_exp = profile.get('experience')

        user = User(age, height, weight, scale, general_health, talk_test, activity_level, hiking_exp)
        age_verify = AgeVerifier()
        if not age_verify.verify_me(user):
            return render_template("user_page.html", age_message=age_verify.print_message())

        comp_verify = CompletionVerifier()
        if not comp_verify.verify_me(user):
            return render_template("user_page.html", completion_message=comp_verify.print_message())

        return render_template("profile.html")


@app.route('/my_profile', methods=['POST', 'GET'])
def calculate_level(user):
    if request.method == 'POST':
        my_level = LevelRecommender()
        my_level.recommend_me(user)
        return my_level.print_message()

if __name__ == "__main__":
    app.run(debug=True)
