# 4-3 20까지 세기
for num in range(1, 21):
    print(num)
print()

# 4-4 백만
# nums = [num for num in range(1, 1000001)]
# print(nums)
# for num in nums:
#     print(num)
# print()

# 4-5 백만까지 더하기
nums = [num for num in range(1, 1000001)]
print("min: ", min(nums))
print("max: ", max(nums))
print("sum: ", sum(nums))
print()

# 4-6 홀수
odds = [num for num in range(1, 21, 2)]
print(odds)
print()

# 4-7 333
threes = [num for num in range(3, 31) if num % 3 == 0]
print(threes)
print()

# 4-8 세제곱
cube = [num**3 for num in range(1, 11)]
print(cube)
print()

# 4-9 세제곱 내포