#from electric_car import Car, ElectricCar
#import electric_car as ec
#import numpy as np
#from electric_car import * # 잘 사용하지 않는다
from car import Car
from electric_car import ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())