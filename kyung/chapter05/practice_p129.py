# 5-1 조건 테스트
food = "cookie"
print("Is food == 'cookie', I predict True")
print(food == 'cookie')

food = "ham"
print("Is food == 'ham', I predict True")
print(food == 'ham')

food = "cola"
print("Is food == 'cola', I predict True")
print(food == 'cola')

food = "cider"
print("Is food == 'cider', I predict True")
print(food == 'cider')

food = "jelly"
print("Is food == 'jelly', I predict True")
print(food == 'jelly')

##

food = "cookie"
print("Is food == 'ham', I predict False")
print(food == 'ham')

food = "cookie"
print("Is food == 'cola', I predict False")
print(food == 'cola')

food = "cookie"
print("Is food == 'cider', I predict False")
print(food == 'cider')

food = "cookie"
print("Is food == 'rice', I predict False")
print(food == 'rice')

food = "cookie"
print("Is food == 'curry', I predict True")
print(food == 'curry')

print()

# 5-2 더 많은 조건 테스트

## 문자열에 대한 동일성 테스트와 비동일성 테스트
str = "string"
print("str == 'string': True ", str == 'string')
print("str == 'character': False ", str == 'character')
print()

## lower() 메서드를 사용한 테스트
name = "Kyung"
print("name == 'kyung': False ", name == 'kyung')
print("name.lower() == 'kyung': True ", name.lower() == 'kyung')
print()

## 일치, 불일치, 이상, 이하, 초과, 미만이 모두 포함된 산술 비교 테스트
num1 = 1
num2 = 2
print("num1 == num2: False ", num1 == num2)
print("num1 != num2: True ", num1 != num2)
print("num1 <= num2: True ", num1 <= num2)
print("num1 >= num2: False ", num1 >= num2)
print("num1 < num2: True ", num1 < num2)
print("num1 > num2: False ", num1 > num2)
print()

## and 키워드와 or 키워드를 사용한 테스트
print("1 != 2 and 3 != 4: True ", 1 != 2 and 3 != 4)
print("1 != 2 or 3 == 4: True ", 1 != 2 or 3 == 4)
print()

## 요소가 리스트에 있는지 확인하는 테스트
list = ['1', '2', '3', '4']
print('1' in list)

## 요소가 리스트에 없는지 확인하는 테스트
print('5' not in list)