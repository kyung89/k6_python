# 책에 없는 부분

class Person:

    count = 0 # 클래스 변수: 함수 바깥에 있다

    def __init__(self, name, age, address):  # 생성자 역할
        self.name = name # 인스턴스 변수: 함수 내에 있다
        self.age = age
        self.address = address
        self.weight = [1,2,3,4,5,6,7] # 공개 속성
        self.__vision = 1.0 # private 속성
        print("{} 객체가 생성됨".format(self.name))
        Person.count += 1 # 클래스 변수를 증가시킴
    
    def __str__(self): # Person 은 객체, 출력 시 필요한 것은
        return f"이름은 {self.name}, 나이는 {self.age}, 주소는 {self.address}, 몸무게는 {self.weight}, 시력은 {self.__vision} 입니다."
        
    def __call__(self):
        return print(f"이름은 {self.name}, 나이는 {self.age}, 주소는 {self.address}, 몸무게는 {self.weight}, 시력은 {self.__vision}")

    def __len__(self):
        return len(self.weight)
    
    def show_person_vision(self):
        print("시력은 {}".format(self.__vision))

    def __eq__(self, other):
        return self.age == other.age
    
    @classmethod # decorator: 자바에서는 annotation(자바 컴파일러한테 알린다! 라는 의미)
    def printing(cls): # cls 고정. self 가 들어가는 딴 메서드와 달리 cls 라는 변수가 들어간다
        print("객체수는 {}".format(cls.count))

    def __getitem__(self, index):
        return self.weight[index]
    
    def __del__(self): # 소멸자. 거의 쓸 일은 없다
        print("객체 {} 이 소멸되었습니다.".format(self.name))


Person("guest", 11, "jeju") # 객체를 만들었는데 가리키는 참조변수가 없다: 만들어지자마자 garbage collection 의 대상이 된다
print()

new_person = Person("ock kyung lim", 34, "busan")
print("이 사람은 {}".format(new_person.name))
print(f"몸무게는 {new_person.weight}")
# print("시력은 {}".format(new_person.__vision))
new_person.show_person_vision()
print()

print(str(new_person)) # __str__() 를 호출한다
print(new_person.__str__())
print(new_person) # string 으로 자동 변환
print()

# my_list = [1,2,3,4]
print(f"리스트 길이: {len(new_person)}") # __len__() 를 호출한다
print()

other_person = Person("yang ha nul", 34, "seoul")
print(new_person == other_person) # __eq__() 를 호출한다: 나이로 비교하기
print()

new_person() # __call__() 를 호출한다: 객체를 함수처럼 호출
print()

# __init__
# __len__
# __str__
# __call__ : 머신러닝에서 많이 쓰인다
# __getitem__ : 많이 쓰인다
# __eq__
# __del__ : 소멸자. 거의 쓸 일은 없다

print(f"new_person[2]: {new_person[2]}") # __getitem__ 을 호출한다: 클래스[인덱스] 실행 시 호출
print()

# 프로그램이 끝나면 자동으로 객체가 소멸된다: __del__() 호출
# garbage collection: 사용되지 않는 객체들은 자동으로 수거된다.

print("객체의 타입은 {}".format(isinstance(new_person, Person)))
print(f"person 객체의 나이는 **{new_person.age:5}***")
print()

# 자바 클래스 static: 클래스 변수, 클래스 메서드
# 파이썬에서는 클래스 변수(함수 바깥에 정의): 중요중요!
print(f"클래스 변수 Person.count: {Person.count}")
print(f"클래스 변수 new_person.count: {new_person.count}")
print(f"클래스 변수 other_person.count: {other_person.count}")
print()
# 파이썬에서의 클래스 메서드: 잘 사용되지는 않는다, @classmethod decorator 를 클래스 메서드 앞에 붙인다
Person.printing() # 클래스 메서드 호출
new_person.printing()
other_person.printing()
print()