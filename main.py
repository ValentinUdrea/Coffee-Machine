MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 7.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 12,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 15,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#Checking if the resources are sufficient for
#We have to loop throw each of the ingredients and see if there
        #is enough resources left
def check_resources_sufficient(order_ingredients):
    """Returns True if there are enough resources and false if not"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True




def process_coins():
    """Returns the total calculated form coins inserted."""
    print("Please insert money.")
    total = int(input("How many lei?: "))
    total += int(input("How many bani?: ")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    """Return True when the payment is acceppted, return false if he money is insufficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"Here is {change} lei in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from te resources"""
    for item in order_ingredients:
        resources[item] -=  order_ingredients[item]
    print(f"Here is you {drink_name}☕")


is_on = True

#Ask the user what coffee whould he like

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    #Turn off the machine if the user enters off
    if choice == "off":
        is_on = True
    #We should be able to print a report of the remaining resources
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: {profit} lei")
    else:
        drink = MENU[choice]
        if check_resources_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])







