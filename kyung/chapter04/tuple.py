# 2024-02-29

def test():
    return (10,20)

a,b = test() # tuple 값을 리턴함
print(f"a = {a}")
print(f"b = {b}")
print()

lst = ['a', 'b', 'c', 'd']
for i, value in enumerate(lst): # enumerate() 함수가 tuple 을 리턴한다
    print(f"i = {i}, value = {value}")
print()

# 0 -> false
# 0.0 -> false
# 빈 컨테이너 = 빈 문자열(""), 빈 리스트([]), 빈 튜플(()), 빈 set({}) -> false

def get_formatted_name(first_name, last_name):
    """실제 이름을 깔끔한 형식으로 반환합니다."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")

# mutable, immutable  정리 필요
