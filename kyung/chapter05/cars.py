cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars: 
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print()

age = 17
if age < 4:
    print("too young")
elif age < 18:
    print("no for vote")
else:
    print("yes for vote")
print()

def greet_user(username):
    """인삿말"""    
    print(f"hello {username}")

greet_user("경림")
help(greet_user)
print(greet_user.__doc__)