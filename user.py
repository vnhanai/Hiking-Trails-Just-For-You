# Author: Ai Vu
# Date: 11/1/2020
# Description: This file includes all classes and their functions to deal with User profile and recommendation


class User:
    """
    represents a user with 8 personal data to decide the fitness level.
    """
    def __init__(self, age, height, weight, scale, talk_test, activity_level, hiking_exp, general_health):
        self._age = age
        self._height = height
        self._weight = weight
        self._scale = scale
        self._talk_test = talk_test
        self._activity_level = activity_level
        self._hiking_exp = hiking_exp
        self._general_health = general_health

    def set_age(self, new_age):
        """sets age which has an int type"""
        self._age = new_age

    def set_height(self, new_height):
        """sets height, which is set in meter and is a float type """
        self._height = new_height

    def set_weight(self, new_weight):
        """sets weight, which is set in kg and is a float type"""
        self._weight = new_weight

    def set_scale(self, new_scale):
        """sets users' self-report of activity's intensity on a scale from 1 to 10,
        which 10 is the highest intensity. This is an int type"""
        self._scale = new_scale

    def set_talk_test(self, new_talk_test):
        """sets users' self-report of activity's intensity based on breathing difficulties, this is a string type"""
        self._talk_test = new_talk_test

    def set_activity_level(self, new_activity):
        """sets activity level, which has a string type"""
        self._activity_level = new_activity

    def set_hiking_exp(self, new_hiking_exp):
        """sets hiking experience, which is a string type"""
        self._hiking_exp = new_hiking_exp

    def set_general_health(self, new_health):
        """sets the medical health reported"""
        self._general_health = new_health

    def get_age(self):
        return self._age

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weight

    def get_talk_test(self):
        return self._talk_test

    def get_scale(self):
        return self._scale

    def get_activity_level(self):
        return self._activity_level

    def get_hiking_exp(self):
        return self._hiking_exp

    def get_general_health(self):
        return self._general_health

    def calculate_bmi(self):
        """returns BMI which is a float type"""
        return self._weight/(self._height**2)

    def calculate_maximal_heart_rate(self):
        """returns maximal heart rate, which is an int type"""
        return 220-self._age


class Recommender:
    def __init__(self):
        pass

    def recommend_me(self, user):
        return None


class LevelRecommender(Recommender):
    """fitness level recommender is a type of Recommender"""
    def __init__(self):
        self._level = ""
        self.message = ""
        self.score = 0

    def recommend_me(self, user):
        """use User data to calculate total score, which then is used to decide fitness level"""
        if user.get_talk_test() == "breathe hard but still can talk":
            self.score += 1
        if user.get_talk_test() == "rapidly breathe and can not hold the talk":
            self.score += 2
        if 4 <= user.get_scale() <= 6:
            self.score += 1
        if 7 <= user.get_scale() <= 10:
            self.score += 2
        if user.get_activity_level() == "Active adult":
            self.score += 1
        if user.get_activity_level() == "Athletic":
            self.score += 2
        if user.get_activity_level() == "Elite Athletic":
            self.score += 3
        if user.get_general_health() == "healthy":
            self.score += 1
        if user.get_hiking_exp() == "Yes":
            self.score += 1
        if 18.5 <= user.calculate_bmi() <= 29.9:
            self.score += 1
        if 6 <= user.get_age() <= 65:
            self.score += 1

        self.message = "Here is recommendations for you: \n" + \
                       "Your maximal heart rate by age is " + str(user.calculate_maximal_heart_rate()) + "\n"

        if 0 <= self.score <= 4:
            self._level = LevelScale.LOW
            self.message += "Your fitness level is " + str(self._level) + "\n" \
                            "Your target heart rate is from " + str(user.get_age()) + " to " + "\n" +\
                            str(int(0.5 * (user.calculate_maximal_heart_rate())))
        if 5 <= self.score <= 7:
            self._level = LevelScale.MODERATE
            self.message += "Your fitness level is " + str(self._level) + "." + "\n" +\
                            "Your target heart rate is from " + str(int(0.5*user.calculate_maximal_heart_rate())) + "\n" + \
                            " to " + str(int(0.7*user.calculate_maximal_heart_rate()))
        else:
            self._level = LevelScale.VIGOROUS
            self.message += "Your fitness level is " + str(self._level) + "." + "\n" +\
                            "Your target heart rate is from " + str(int(0.71*user.calculate_maximal_heart_rate()))+ \
                            " to " + str(int(0.85*user.calculate_maximal_heart_rate()))

    def print_message(self):
        return self.message


class LevelScale:

    LOW = "low level. You are encouraged to regularly exercise " \
          "and gradually increase the intensity to reach the moderate level. \
          If possible, you should hike with a companion."

    MODERATE = "moderate level. Your recommended time for weekly exercise is 150 minutes or more " \
               "with a targeted heart rate of 50-70% of our maximum heart rate by age."

    VIGOROUS = "vigorous level. Your recommended time for weekly exercise is 75 minutes or more " \
               "with a targeted heart rate of 71-85 % of our maximum heart rate by age."


class Message:
    """represents message that the system presents for user on the UI"""
    def __init__(self):
        pass

    def print_message(self):
        pass


class Verifier:
    """represent verifier who will verify if user's input is valid and complete as required """
    def __init__(self):
        pass

    def verify_me(self, user):
        return True


class AgeVerifier:
    """AgeVerifier is a type of Verifier"""

    def __init__(self):
        self.MINIMAL_AGE = 6
        self.message = ""

    def verify_me(self, user):
        my_age = user.get_age()
        if my_age < self.MINIMAL_AGE:
            self.message = "You're not old enough to use this fitness level recommendation"
            return False
        return True

    def print_message(self):
        return self.message


class CompletionVerifier:
    """CompletionVerifier is a type of Verifier"""

    def __init__(self):
        self.message = ""

    def verify_me(self, user):
        if user.get_age() is 0 or user.get_activity_level() is None \
            or user.get_height() is 0 or user.get_weight() is 0 \
                or user.get_hiking_exp() is None or user.get_scale() is 0 \
                or user.get_talk_test() is None or user.get_general_health() is None:
            self.message = "All of questions need to be filled for calculating fitness level recommendation for you"
            return False
        return True

    def print_message(self):
        return self.message

