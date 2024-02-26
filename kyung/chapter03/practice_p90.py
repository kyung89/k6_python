# 3-8 세상 구경
print("# 3-8 세상 구경")
places = ['busan', 'seoul', 'daejeon', 'daegu', 'jeju']

print("원래 순서 출력: ")
print(places)
print()

print("sorted() 출력: ")
print(sorted(places))
print()

print("다시 출력(변하지 않음): ")
print(places)
print()

print("sorted() reverse 출력: ")
print(sorted(places, reverse=True))
print()

print("다시 출력(변하지 않음): ")
print(places)
print()

print("reverse() 적용: ")
places.reverse()
print(places)
print()

print("reverse() 다시 적용: ")
places.reverse()
print(places)
print()

print("sort()를 사용하여 출력: ")
places.sort()
print(places)
print()

print("sort()를 사용하여 역순 출력: ")
places.sort(reverse=True)
print(places)
print()

# 3-9 저녁 식사 손님
people = ['양하늘', '구애진', '구희진', '선미진', '김호인', '이진섭']
print(f"저녁식사에 {len(people)} 명을 초대합니다.")
print()

# 3-10 함수 연습
hamsters = ['dwarf', 'roborovski', 'pandamouse', 'saphire', 'pudding', 'pearl']
hamsters.sort()
print(hamsters)
print(hamsters[-2])
print()
# 추가로 함수와 메서드 사용