def make_pizza(size, *toppings):
    # print(toppings)
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# make_pizza("pepperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")