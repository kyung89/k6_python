# 2-3 개별 메시지
print("# 2-3 개별 메시지")
kyung = "경림"
kyungMsg = f"안녕하세요. {kyung}, 오늘 파이썬을 배워 보는 게 어떨까요?"
print(kyungMsg)
print()

# 2-4 이름의 대소문자
print("# 2-4 이름의 대소문자")
name = "kyung"
print("대문자 출력: ", name.upper())
print("소문자 출력: ", name.lower())
print("첫 글자만 대문자 출력: ", name.title())
print()

# 2-5 명언
print("# 2-5 명언")
text = '알베르트 아인슈타인, "한 번도 실수한 적이 없는 사람은 한 번도 새로운 것에 도전애 본 것이 없는 사람이다"'
print(text)
print()

# 2-6 명언2
print("# 2-6 명언2")
famous_person = "알베르트 아인슈타인의 복제"
message = f'{famous_person} , "한 번도 실수한 적이 없는 사람은 한 번도 새로운 것에 도전애 본 것이 없는 사람이다"'
print(message)
print()

# 2-7 이름에서 공백 제거
print("# 2-7 이름에서 공백 제거")
example_name = "\t김요안나\t\n"
print(example_name)
print(example_name.lstrip())
print(example_name.rstrip())
print(example_name.strip())
print()

# 2-8 파일 확장자
print("# 2-8 파일 확장자")
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
print()