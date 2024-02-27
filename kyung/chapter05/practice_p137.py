# 5-3 외계인 색깔 #1
alien_color = "green"
if alien_color == "green": print("플레이어가 5점을 획득했습니다.")

alien_color = "red"
if alien_color == "green": print("플레이어가 5점을 획득했습니다.")
print()

# 5-4 외계인 색깔 #2
alien_color = "green"

if alien_color == "green": print("플레이어가 5점을 획득했습니다.")
if alien_color != "green": print("플레이어가 10점을 획득했습니다.")

if alien_color == "green" : print("플레이어가 5점을 획득했습니다.")
else: print("플레이어가 10점을 획득했습니다.")
print()

# 5-5 외계인 색깔 #3
alien_color = "green"
if alien_color == "green": print("플레이어가 5점을 획득했습니다.")
elif alien_color == "yellow": print("플레이어가 10점을 획득했습니다.")
elif alien_color == "red": print("플레이어가 15점을 획득했습니다.")
print()
alien_color = "yellow"
if alien_color == "green": print("플레이어가 5점을 획득했습니다.")
elif alien_color == "yellow": print("플레이어가 10점을 획득했습니다.")
elif alien_color == "red": print("플레이어가 15점을 획득했습니다.")
print()
alien_color = "red"
if alien_color == "green": print("플레이어가 5점을 획득했습니다.")
elif alien_color == "yellow": print("플레이어가 10점을 획득했습니다.")
elif alien_color == "red": print("플레이어가 15점을 획득했습니다.")
print()

# 5-6 삶의 단계
age = 10
if age < 2: print("영아")
elif age >= 2 and age < 4: print("유아")
elif age >=4 and age < 13: print("어린이")
elif age >= 13 and age < 20: print("십대")
elif age >= 20 and age < 65: print("성인")
else: print("노인")
print()

# 5-7 좋아하는 과일
favorite_fruits = ['apple', 'banana', 'peach', 'orange']
if 'apple' in favorite_fruits: print("당신은 사과를 무척 좋아하네요!")
if 'banana' in favorite_fruits: print("당신은 바나나를 무척 좋아하네요!")
if 'peach' in favorite_fruits: print("당신은 복숭아를 무척 좋아하네요!")
if 'orange' in favorite_fruits: print("당신은 오렌지를 무척 좋아하네요!")
if 'mellon' in favorite_fruits: print("당신은 멜론를 무척 좋아하네요!")