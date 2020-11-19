from flask import Flask
from flask import render_template, request, redirect

from ai.user import User, AgeVerifier, CompletionVerifier, LevelRecommender

app = Flask(__name__)

user = User(age=None,
            height=None,
            weight=None,
            scale=None,
            general_health=None,
            talk_test=None,
            activity_level=None,
            hiking_exp=None)


@app.route('/')
def home():
    return render_template("trails.html");


@app.route('/profile')
def profile():
    return render_template("user_page.html");


@app.route("/user_profile", methods=['POST', 'GET'])
def user_profile():
    if request.method == 'GET':
        return render_template("user_page.html")

    if request.method == 'POST':
        profile = request.form
        age = profile.get('age')
        if len(age) > 0:
            user.set_age(int(age))
        height = profile.get('height')
        if len(height) > 0:
            user.set_height(float(height))
        weight = profile.get('weight')
        if len(weight) > 0:
            user.set_weight(float(weight))
        scale = profile.get('scale')
        if len(scale) > 0:
            user.set_scale(int(scale))
        user.set_general_health(profile.get('health'))
        user.set_talk_test(profile.get('talk'))
        user.set_activity_level(profile.get('activity'))
        user.set_hiking_exp(profile.get('experience'))

        age_verify = AgeVerifier()
        print(user.get_age())
        if not age_verify.verify_me(user):
            return render_template("user_page.html", age_message=age_verify.print_message())

        comp_verify = CompletionVerifier()
        if not comp_verify.verify_me(user):
            return render_template("user_page.html", completion_message=comp_verify.print_message())

        return redirect('/my_profile')


@app.route('/my_profile', methods=['POST', 'GET'])
def calculate_level():
    my_level = LevelRecommender()
    my_level.recommend_me(user)
    return render_template("my_profile.html", level=my_level.print_message())


if __name__ == "__main__":
    app.run(debug=True)
