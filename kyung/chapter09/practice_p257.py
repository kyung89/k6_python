# 9-13 주사위
from random import randint

class Die:
    def __init__(self, sides):
        self.sides = sides
    
    def roll_die(self): 
        print(f"주사위 수는 {randint(1,self.sides)}")

print("<6면체 주사위>")
die_six = Die(6)
for i in range(0, 10): die_six.roll_die()
print()

print("<10면체 주사위>")
die_ten = Die(10)
for i in range(0, 10): die_ten.roll_die()
print()

print("<20면체 주사위>")
die_twenty = Die(20)
for i in range(0, 10): die_twenty.roll_die()
print()

# 자바 로또 파이썬으로 구현하기
class Lotto:
    def __init__(self):
        self.numbers = []
        for i in range(0,7): self.numbers.append(randint(1,46))
    
    def print_numbers(self):
        print(f"{self.numbers}")

lotto = Lotto()
lotto.print_numbers()
print()

# 9-14 복권
from random import choice
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'sunshine', 'rain', 'cloud', 'wind', 'bee']
is_same = []
for i in range(0, 4):
    rnd = choice(list)
    is_same.append(rnd)

print(f"{is_same} 에 일치하는 티켓에 상금을 지급합니다.")
print()

# 9-15 복권 분석
my_ticket = [3,4,5, 'rain']

while len(my_ticket) != 0:
    rnd = choice(list)
    if rnd == my_ticket[0]:
        print(f"{rnd} 가 일치했습니다. my_ticket에서 해당 숫자/문자를 꺼냅니다.")
        my_ticket.pop(0)
    else:
        print(f"{rnd} 와 일치하는 것이 없습니다.")

# 9-16 이번 주의 파이썬 모듈