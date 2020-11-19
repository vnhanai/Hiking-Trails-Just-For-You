# Author: Ai Vu
# Date: 10/3/2020
# Description: This is the test case for an adult user
# who filled all questions and who misses answering a question.

from ai.user import User, AgeVerifier, CompletionVerifier, LevelRecommender
print("Test Case1" + "\n")
user_1 = User(age=30, height=170, weight=80, scale=8,
              general_health="healthy", talk_test = "rapidly breathe and can not hold the talk",
              activity_level="Active adult", hiking_exp="Yes")

age_verify_1 = AgeVerifier()
if not age_verify_1.verify_me(user_1):
    print(age_verify_1.print_message())

comp_verify_1 = CompletionVerifier()
if not comp_verify_1.verify_me(user_1):
    print(comp_verify_1.print_message())
else:
    my_level_1 = LevelRecommender()
    my_level_1.recommend_me(user_1)
    print(my_level_1.print_message())

print("Test Case2")
user_2 = User(age=25, height=170, weight=0, scale=7,
              general_health="healthy", talk_test = "rapidly breathe and can not hold the talk",
              activity_level="Active adult", hiking_exp="Yes")

age_verify_2 = AgeVerifier()
if not age_verify_2.verify_me(user_2):
    print(age_verify_2.print_message())

comp_verify_2 = CompletionVerifier()
if not comp_verify_2.verify_me(user_2):
    print(comp_verify_2.print_message())
else:
    my_level_2 = LevelRecommender()
    my_level_2.recommend_me(user_2)
    print(my_level_2.print_message())




