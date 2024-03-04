class Dog:
    """개 클래스"""

    def __init__(self, name, age):
        """name 과 age 속성 초기화"""
        self.name = name # 속성 > 자바의 클래스 field 에 해당된다
        self.age = age # 속성
        self.__price = 100
    
    def sit(self):
        """앉기"""
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        """구르기"""
        print(f"{self.name} rolled over!")

my_dog = Dog("Willie", 6)
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
#print(f"My dog price: {my_dog.__price}")
print()

your_dog = Dog("Lucy", 3)
your_dog.sit()
your_dog.roll_over()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
#print(f"Your dog price: {your_dog.__price}")
print()