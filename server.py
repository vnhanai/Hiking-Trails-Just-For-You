from flask import Flask, render_template, request, redirect
from trail_api import Trail, TrailList, Trail_API
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("user_page.html");

@app.route('/trails', methods=['GET', 'POST'])
def trails():
    if request.method == 'GET':
        la_latitude = 40.0274
        la_longitude = -105.2519
        # Default location is LA
        myTrails = Trail_API(la_latitude, la_longitude)
        return render_template("trails.html", trails=myTrails.getTrails().getAllTrails())
    elif request.method == 'POST':
        # We will have to get the lat and long from the user
        latitude = 0
        longitude = 0
        myTrails = Trail_API(latitude, longitude)
        trails = myTrails.getTrails()
        return render_template("trails.html")

if __name__ == "__main__":
    app.run();
    