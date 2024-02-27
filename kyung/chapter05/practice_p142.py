# 5-8 관리자
users = ['ock', 'lee', 'choi', 'park', 'admin']
for user in users:
    if user == "admin": 
        print("관리자님 안녕하세요 상태 보고서를 보시겠습니까?")
    else: 
        print(f"{user} 님 안녕하세요, 다시 로그인해주셔서 감사합니다.")
print()

# 5-9 사용자 없음
users = []
if not users: 
    print("사용자가 있어야 합니다.")
users = ['kim', 'lee', 'choi', 'ock']
if not users: 
    print("사용자가 있어야 합니다.")
else: 
    print("사용자가 있습니다.")
users.pop()
users.pop()
users.pop()
users.pop()
if not users: print("사용자가 있어야 합니다.")
print()

# 5-10 사용자 이름 체크
current_users = ['ock', 'lee', 'choi', 'park', 'admin']
new_users = ['ock', 'lee', 'lucky', 'sam', 'kim']
for user in new_users: 
    if user in current_users: 
        print("새 사용자 이름을 입력하세요.")
    else: 
        print(f"{user} 은 사용할 수 있습니다.")
print()
current_users2 = [user.lower() for user in current_users]
new_users2 = ['ock', 'LEE', 'lucky', 'sam', 'kim']
for user in new_users: 
    if user.lower() in current_users2: 
        print("새 사용자 이름을 입력하세요.")
    else: 
        print(f"{user} 은 사용할 수 있습니다.")
print()
# 5-11 서수
numbers = ["1st", "2nd", "3rd"]
for num in range(4, 10):
    numbers.append(str(num) + 'th')
print(numbers)