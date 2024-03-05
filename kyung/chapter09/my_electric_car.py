from electric_car import ElectricCar, Battery

my_leaf= ElectricCar("nissan", "leaf", 2024)
print(f"전기차는 {my_leaf.get_descriptive_name()}")
print("전기차는 {}".format(my_leaf.get_descriptive_name()))
my_leaf.battery.describe_battery() # 하위 구성 객체 사용

large_car= ElectricCar("bentz", "e200", 2023, Battery(65))
print(large_car.get_descriptive_name())
large_car.battery.describe_battery() # 하위 구성 객체 사용

my_leaf.battery.get_range()
large_car.battery.get_range()