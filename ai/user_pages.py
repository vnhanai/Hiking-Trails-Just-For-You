from flask import Flask
from flask import render_template, request, redirect, url_for
from new_user import Account, User, Activity, BMI, Health, Intensity, LevelRecommend, LevelScale
import sqlite3
import constant


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
    return render_template("user_page.html")


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
    level.my_level(score)
    my_id = account.get_email()
    my_fitness_level = level.get_message()
    conn = sqlite3.connect('new_user.db')
    c = conn.cursor()
    sql_str = "INSERT INTO {table} VALUES('{id}', '{level}')".format(table=constant.USER_TABLE,
                                                                     id=my_id, level=my_fitness_level)
    # print(sql_str)
    c.execute(sql_str)
    conn.commit()
    conn.close()

    return render_template("my_profile.html", level=level.get_message())


@app.route('/old_user', methods=['POST', 'GET'])
def get_old_user():
    if request.method == 'GET':
        return render_template("old_user.html")

    if request.method == 'POST':
        my_profile = request.form
        email = my_profile.get('email')
        account.set_email(email)
        conn = sqlite3.connect(constant.DB_NAME)
        c = conn.cursor()
        print('email ', email)
        c.execute("SELECT * FROM users WHERE id =:id", {'id': email})
        user_record = c.fetchone()
        print('user_record', user_record)
        conn.commit()
        conn.close()
        return render_template("old_user_rec.html", level_record=user_record[1])


@app.route('/old_user_rec', methods=['POST', 'GET'])
def get_record():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    with conn:
        # c.execute("SELECT * FROM users WHERE Id =:Id", {'Id': my_id})
        # c.execute("INSERT INTO users VALUES(':Id', ':level')", {'Id': my_id, 'level': my_fitness_level})
        return render_template("old_user_rec.html", level_record=c.fetchone())


if __name__ == "__main__":
    app.run(debug=True)

