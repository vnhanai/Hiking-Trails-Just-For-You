from flask import Flask
from flask import render_template, request, redirect

from newUser import Account, User, Activity, BMI, Health, Intensity, LevelRecommend, LevelScale

app = Flask(__name__)
account = Account()
user = User(age=None)
activity = Activity(hiking_experience=None, activity_level=None)
bmi = BMI(weight=None, height=None)
health = Health(medical_health=None)
intensity = Intensity(scale=None, talk_test=None)
level = LevelScale(user)
my_level = LevelRecommend(user, bmi, activity, intensity, health)


@app.route('/')
def home():
    return render_template("trails.html")


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    return render_template("user_page.html");


@app.route("/user_profile", methods=['POST', 'GET'])
def user_profile():
    if request.method == 'GET':
        return render_template("user_page.html")

    if request.method == 'POST':
        my_profile = request.form
        email = my_profile.get('email')
        account.set_email(email)
        age = my_profile.get('age')
        if len(age) > 0:
            user.set_age(int(age))
        height = my_profile.get('height')
        if len(height) > 0:
            bmi.set_height(float(height))
        weight = my_profile.get('weight')
        if len(weight) > 0:
            bmi.set_weight(float(weight))
        scale = my_profile.get('scale')
        if len(scale) > 0:
            intensity.set_scale(int(scale))
        health.set_medical_health(my_profile.get('health'))
        intensity.set_talk_test(my_profile.get('talk'))
        activity.set_activity_level(my_profile.get('activity'))
        activity.set_hiking_exp(my_profile.get('experience'))

        if not account.verify_me():
            return render_template("user_page.html", email_message=account.get_message())

        if not user.verify_me():
            return render_template("user_page.html", age_message=user.get_message())

        if not my_level.verify_me():
            return render_template("user_page.html", completion_message=my_level.get_message())

        return redirect('/my_profile')


@app.route('/my_profile', methods=['POST', 'GET'])
def calculate_level():
    score = my_level.my_fitness_level()
    fitness_score = level.my_level(score)
    return render_template("my_profile.html", level=level.get_message())


if __name__ == "__main__":
    app.run(debug=True)
