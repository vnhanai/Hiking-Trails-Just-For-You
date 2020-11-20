# Author: Ai Vu
# Date: 11/14/2020
# Description: correct code smells from user.py


class Message:
    """represents message that the system presents for user on the UI"""

    def __init__(self):
        pass

    def get_message(self):
        pass


class Verifier:
    """represent verifier who will verify if user's input is valid and complete as required """

    def __init__(self, ver):
        self._ver = ver

    @staticmethod
    def verify_me():
        return True


class Account:
    def __init__(self):
        self._email = ''
        self._message = ''

    def set_email(self, my_email):
        self._email = my_email

    def get_email(self):
        return self._email

    def verify_me(self):
        if self.get_email() == '' or self.get_email() is None:
            self._message = "Email address is required to save your personal profile"
            return False
        return True

    def get_message(self):
        return self._message


class User:
    MINIMAL_AGE = 6

    def __init__(self, age):
        self._age = age
        self._message = ''
        self._score = 0

    def set_age(self, new_age):
        """sets age which has an int type"""
        self._age = new_age

    def get_age(self):
        return self._age

    def age_score(self):
        if self._age <= 65:
            self._score = 1
        else:
            self._score = 0
        return self._score

    def verify_me(self):
        my_age = self.get_age()
        if my_age is not None and my_age < self.MINIMAL_AGE:
            self._message = "You're not old enough to use this fitness level recommendation"
            return False
        return True

    def calculate_maximal_heart_rate(self):
        """returns maximal heart rate, which is an int type"""
        maximal_heart_rate = 220 - self._age
        return maximal_heart_rate

    def target_heart_rate(self, percent):
        target_heart_rate = int(percent * self.calculate_maximal_heart_rate())
        return target_heart_rate

    def get_message(self):
        return self._message


class BMI:
    def __init__(self, weight, height):
        self._height = height
        self._weight = weight
        self._score = 0

    def set_height(self, new_height):
        """sets height, which is set in meter and is a float type """
        self._height = new_height

    def set_weight(self, new_weight):
        """sets weight, which is set in kg and is a float type"""
        self._weight = new_weight

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weight

    def bmi_score(self, under_bmi=18.5, over_bmi=29.9):
        """returns BMI which is a float type"""
        if under_bmi <= self._weight / ((self._height * 0.01) ** 2) <= over_bmi:
            self._score = 1
        else:
            self._score = 0
        return self._score


class Health:
    HEALTHY = "healthy"

    def __init__(self, medical_health):
        self._medical_health = medical_health
        self._score = 0

    def set_medical_health(self, new_health):
        """sets the medical health reported"""
        self._medical_health = new_health

    def get_medical_health(self):
        return self._medical_health

    def healthy_score(self):
        if self._medical_health == Health.HEALTHY:
            self._score = 1
        else:
            self._score = 0
        return self._score


class Activity:
    ACTIVE_ADULT = "Active adult"
    ATHLETIC = "Athletic"
    ELITE_ATHLETIC = "Elite athletic"
    HEALTH_SEEKER = "Health seeker"

    def __init__(self, hiking_experience, activity_level):
        self._activity_level = activity_level
        self._hiking_exp = hiking_experience
        self._score = 0

    def set_activity_level(self, new_activity):
        """sets activity level, which has a string type"""
        self._activity_level = new_activity

    def set_hiking_exp(self, new_hiking_exp):
        """sets hiking experience, which is a string type"""
        self._hiking_exp = new_hiking_exp

    def get_activity_level(self):
        return self._activity_level

    def get_hiking_exp(self):
        return self._hiking_exp

    def activity_level_score(self):
        if self._activity_level == Activity.ACTIVE_ADULT:
            self._score = 1
        if self._activity_level == Activity.ATHLETIC:
            self._score = 2
        if self._activity_level == Activity.ELITE_ATHLETIC:
            self._score = 3
        else:
            self._score = 0
        return self._score

    def hiking_score(self):
        if self._hiking_exp == "Yes":
            self._score = 1
        else:
            self._score = 0
        return self._score


class Intensity:
    EASY_BREATHE = "easy breathe and talk"
    MEDIUM_BREATHE = "breathe hard but still can talk"
    HARD_BREATHE = "rapidly breathe and can not hold the talk"

    def __init__(self, scale, talk_test):
        self._scale = scale
        self._talk_test = talk_test
        self._score = 0

    def set_scale(self, new_scale):
        """sets users' self-report of activity's intensity on a scale from 1 to 10,
        which 10 is the highest intensity. This is an int type"""
        self._scale = new_scale

    def set_talk_test(self, new_talk_test):
        """sets users' self-report of activity's intensity based on breathing difficulties, this is a string type"""
        self._talk_test = new_talk_test

    def get_talk_test(self):
        return self._talk_test

    def get_scale(self):
        return self._scale

    def talk_test_score(self):
        if self._talk_test == self.MEDIUM_BREATHE:
            self._score = 1
        if self._talk_test == self.HARD_BREATHE:
            self._score = 2
        else:
            self._score = 0
        return self._score

    def strenuous_scale(self):
        if 4 <= self._scale <= 6:
            self._score = 1
        if 7 <= self._scale <= 10:
            self._score = 2
        else:
            self._score = 0
        return self._score


class LevelScale:
    LOW = "low level. You are encouraged to regularly exercise " \
          "and gradually increase the intensity to reach the moderate level. \
          If possible, you should hike with a companion."

    MODERATE = "moderate level. Your recommended time for weekly exercise is 150 minutes or more " \
               "with a targeted heart rate of 50-70% of our maximum heart rate by age."

    VIGOROUS = "vigorous level. Your recommended time for weekly exercise is 75 minutes or more " \
               "with a targeted heart rate of 71-85 % of our maximum heart rate by age."

    def __init__(self, user):
        self._message = ''
        self._user = user

    def my_level(self, score):
        if 0 <= score <= 4:
            my_level = LevelScale.LOW
            target_heart_rate = self._user.target_heart_rate(0.5)
        elif 5 <= score <= 7:
            my_level = LevelScale.MODERATE
            target_heart_rate = "from " + str(self._user.target_heart_rate(0.51)) + \
                                " to " + str(self._user.target_heart_rate(0.7))
        else:
            my_level = LevelScale.VIGOROUS
            target_heart_rate = "from " + str(self._user.target_heart_rate(0.71)) + \
                                " to " + str(self._user.target_heart_rate(0.81))
        maximum_heart_rate = self._user.calculate_maximal_heart_rate()
        self._message = "Your fitness level is " + str(my_level) + \
                        " Your maximum heart rate is " + str(maximum_heart_rate) + \
                        ". Your target heart rate is " + str(target_heart_rate)
        return self._message

    def get_message(self):
        return self._message


class LevelRecommend:

    def __init__(self, user, bmi, activity, intensity, health):
        self._user = user
        self._bmi = bmi
        self._activity = activity
        self._intensity = intensity
        self._health = health
        self._message = ""

    def verify_me(self):
        if self._user.get_age() == '' or self._user.get_age() is None \
                or self._activity.get_activity_level() == '' or self._activity.get_activity_level() is None \
                or self._bmi.get_height() == '' or self._bmi.get_height() is None \
                or self._bmi.get_weight() == '' or self._bmi.get_weight() is None \
                or self._activity.get_hiking_exp() == '' or self._activity.get_hiking_exp() is None \
                or self._intensity.get_scale() == '' or self._intensity.get_scale() is None \
                or self._intensity.get_talk_test() == '' or self._intensity.get_talk_test() is None \
                or self._health.get_medical_health() == '' or self._health.get_medical_health() is None:
            self._message = "All of questions need to be filled for calculating fitness level recommendation for you. " \
                            "Please backtrack to fill out the missing date."
            return False
        return True

    def my_fitness_level(self):
        age_score = self._user.age_score()
        bmi_score = self._bmi.bmi_score()
        hiking_score = self._activity.hiking_score()
        activity_score = self._activity.activity_level_score()
        talk_score = self._intensity.talk_test_score()
        strenuous_score = self._intensity.strenuous_scale()
        health_score = self._health.healthy_score()

        total_score = age_score + bmi_score + hiking_score + activity_score + \
                      talk_score + strenuous_score + health_score

        return total_score

    def get_message(self):
        return self._message

