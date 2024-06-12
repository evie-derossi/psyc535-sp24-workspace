"""takes input of weight of bag and tell you T F if it's overweight"""

weight : str = input("What is the weight of your bag in pounds?: ")
weight = float(weight)
max_weight: float = 50.0
overweight: float = weight - max_weight

print("Cleared?: " + str(weight <= max_weight))

if weight > max_weight:
    print("Your bag is " + str(overweight) + " lbs overweight")
else: 
    print("Your bag is cleared!")