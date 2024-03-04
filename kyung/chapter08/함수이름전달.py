# 2024-02-29

# 함수의 매개변수로 함수 전달하기
def ten_times(func):
    for i in range(10):
        func()

def print_hello():
    print("hello")

ten_times(print_hello)
print()

def print_work():
    print("coding")

ten_times(print_work)
print()

def add(x,y):
    return x + y

def minus(x,y):
    return x - y

def apply_operation(operation, x, y): # map() 함수 역할
    return operation(x,y)

print(apply_operation(add, 1, 2))
print(apply_operation(minus, 5, 2))
print()

# 2024-03-04

#  map(), filter() 함수 사용
 
# def power(item):
#     return item * item

# def under_three(item):
#     return item < 3

power = lambda x: x*x
under_three =  lambda x:x<3

lst = [1,2,3,4,5]
map_list = map(power, lst)
print(f"map() 함수 적용결과: {list(map_list)}")

filter_list = filter(under_three, lst)
print(f"filter() 함수 적용결과: {list(filter_list)}")

# step1 함수자체를 인수로 전달
# step2 apply_operation(add, 3, 4) : x, y 전달
# step3 map 사용
# step4 람다식