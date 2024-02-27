for value in range(1, 5):
    print(value)
print()

print("[LIST]")
numbers = list(range(1,6))
print(numbers)
print()

print("[SET]")
numbers = set(range(1,6))
print(numbers)
print()

even_numbers = list(range(2,11,2))
print(even_numbers)
print()

squares = []
for value in range(1,11):
    #square = value ** 2
    #squares.append(square)
    squares.append(value ** 2)
print(squares)
print(value)
print()

squares = [value**2 for value in range(1,20)]
print(squares)
print(squares[0:3]) # slicing
print()

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(my_list[::-1])
print(my_list[::-2])
print(my_list[::-3])
print()

a = [1, 2]
b = [3, 4]
c = a + b        # [1, 2, 3, 4]
print(c)
print()

b = [0]
c = b*5
c 		# [0, 0, 0, 0, 0]
print(c)
print()

a = [1, 2, 3, 4, 5]
b = [3, 4]
#c = a - b # 에러
c1 = [x for x in a if x not in b] # 빼기연산 직접 구현
print("c1: ", c1)
c2 = list(set(a) - set(b))
print("c2: ", c2)
print()

a = [10,20,30,40,50]
b = a # shallow copy
print("b: ", b)
b[0] = 222
print("a: ", a)
a = [10,20,30,40,50]
b = a[:] # deep copy
print("b: ", b)
b[1] =333
print("a: ", a)
print()

a = [[1,2,3],[4,5,6]]
b = a[:] # shallow copy
print("b: ", b)
a[0][0] =333
print("a: ", a)
print("b: ", b)