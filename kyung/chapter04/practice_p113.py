# 4-10 슬라이스

players = ['ock', 'kim', 'lee', 'jang', 'choi']
print("리스트의 첫 세 항목은: ", players[:3])
print("리스트의 중간 세 항목은: ", players[1:4])
print("리스트의 마지막 세 항목은: ", players[-3:])
print()

# 4-11 피자
pizzas = ['cheese', 'hawaian', 'meat']
friend_pizzas = pizzas[:]
pizzas.append('sweet potato')
friend_pizzas.append('hotsauce')
print("내가 좋아하는 피자는: ", pizzas)
print("내 친구가 좋아하는 피자는: ", friend_pizzas)
print()

# 4-12 루프 연습
my_foods = ["pizza", "falafel", "carrot cake"]
# 이해를 못하겠음