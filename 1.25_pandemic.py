"""practice problem"""

case_limit : int = 50
case_num : str = input("How many cases are there?: ")
case_num = int(case_num)
money_min : float = 6.00
money_amnt : str = input ("How much money do you have?: ")
money_amnt = float(money_amnt)

if money_amnt > money_min and case_num < case_limit:
    print("Enjoy the movie!")
else:
    print("Sorry, come back soon!")