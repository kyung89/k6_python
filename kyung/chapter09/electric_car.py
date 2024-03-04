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

my_leaf= ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery() # 하위 구성 객체 사용

large_car= ElectricCar("bentz", "e200", 2023, Battery(65))
print(large_car.get_descriptive_name())
large_car.battery.describe_battery() # 하위 구성 객체 사용

my_leaf.battery.get_range()
large_car.battery.get_range()