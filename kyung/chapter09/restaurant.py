class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The name of restaurant is {self.restaurant_name}")
        print(f"Cuisine type is {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open")

#restaurant = Restaurant("홍콩반점", "중국요리")
#restaurant.describe_restaurant()
#restaurant.open_restaurant()