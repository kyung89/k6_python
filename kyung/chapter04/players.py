players = ['ock', 'kim', 'lee', 'jang', 'choi']

for player in players[:3]:
    print(player.title())
print()

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # deep copy in 1차원
print("my_foods: ", my_foods)
print("friend_foods: ", friend_foods)
print()
my_foods.append("cannoli")
friend_foods.append('ice cream')
print("my_foods: ", my_foods)
print("friend_foods: ", friend_foods)
print()

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods # shallow copy
print("my_foods: ", my_foods)
print("friend_foods: ", friend_foods)
print()
my_foods.append("cannoli")
friend_foods.append('ice cream')
print("my_foods: ", my_foods)
print("friend_foods: ", friend_foods)
print()