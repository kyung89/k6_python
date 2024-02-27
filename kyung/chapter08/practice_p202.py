# 8-3 티셔츠
def make_shirt(size, msg):
    print(f"셔츠의 사이즈는 {size}")
    print(f"메시지는 {msg}")

make_shirt("라지", "코코아 먹기")
make_shirt(size="스몰", msg="신나는 여행")
print()

# 8-4 라지 셔츠
def make_shirt(size, msg="I love python"):
    print(f"셔츠의 사이즈는 {size}")
    print(f"메시지는 {msg}")

make_shirt("라지")
make_shirt("미디엄")
make_shirt("라지", "메시지1")
make_shirt("미디엄", "메시지2")
print()

# 8-5 도시
def describe_city(city, nation="한국"):
    print(f"{city}는 {nation}에 있습니다.")

describe_city("부산")
describe_city("서울")
describe_city("알라배마", "미국")