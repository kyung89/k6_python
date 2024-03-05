# 9-6 아이스크림 가판대
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The name of restaurant is {self.restaurant_name}")
        print(f"Cuisine type is {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
    
    def printFlavors(self):
        for flavor in self.flavors:
            print(flavor)

        print("맛이 {}".format(self.flavors)) # = print(f"맛이 {self.flavors}")

iceCreamStand = IceCreamStand("휘니의 아이스크림 가게", "아이스크림", "딸기맛", "초코맛", "우유맛")
iceCreamStand.printFlavors()
print()

# 9-7 관리자
class User:
    def __init__(self, first_name, last_name, job, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print(f"이름은 {self.get_fullname()} 입니다.")
        print(f"직업은 {self.job} 입니다.")
        print(f"나이는 {self.age} 입니다.")
        print(f"성별은 {self.gender} 입니다.")

    def get_fullname(self):
        return (f"{self.first_name} {self.last_name}").title()
    
    def greet_user(self):
        print(f"{self.get_fullname()} 님 환영합니다.")

class Privileges:
    def __init__(self, *privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        for p in self.privileges:
            print(p)

class Admin(User):
    def __init__(self, first_name, last_name, job, age, gender):
        super().__init__(first_name, last_name, job, age, gender)
        self.privileges = Privileges("can delete post","can add post","can ban user")

admin = Admin("경림", "옥", "프로그래머", 34, "여자")
#admin.show_privileges()
print()

# 9-8 권한
admin = Admin("경림", "옥", "프로그래머", 34, "여자")
admin.privileges.show_privileges()
print()

# 9-9 배터리 업그레이드
class Car:
    """자동차 클래스"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """뜻이 분명하고 깔끔한 이름 반환"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """자동차의 주행거리를 출력합니다"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        거리계 값을 주어진 값으로 바꿉니다.
        현재 값보다 적은 값을 할당할 수 없습니다.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back on odometer!")

    def increment_odometer(self, miles):
        """거리계 값을 주어진 값만큼 늘입니다."""
        self.odometer_reading += miles

class Battery:
    """전기차의 배터리를 표현하는 클래스"""
    def __init__(self, battery_size = 40):
        """배터리 속성을 초기화합니다."""
        self.battery_size = battery_size

    def describe_battery(self):
        """배터리 크기를 설명하는 문자을 출력합니다."""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """이 배터리로 주행할 수 있는 거리를 알려 줍니다."""
        if self.battery_size <= 40:
            range = 150
        elif self.battery_size >= 65: 
            range = 225
        
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65

class ElectricCar(Car):
    """전기차"""
    def __init__(self, make, model, year, large_battery = Battery()): # default parameter
        super().__init__(make, model, year)
        self.battery = large_battery
    
    #def describe_battery(self):
    #    """"배터리 크기를 설명하는 문장을 출력합니다"""
    #    print(f"This car has a {self.battery_size}-kWh battery")

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

car = ElectricCar("nissan", "leaf", 2024)
car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()