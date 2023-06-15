MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
global refund, total_money
profit = 0
refund = 0
ordering = True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total



def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
while ordering:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    order = order.lower()
    if order == "report":
        print(resources)
        print(f"Money: ${profit}")
    elif order == "exit":
        print("Thank you. Have a great day")
        ordering = False
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])

                
    # else:
    #     print("Error! Try again")
        

# def calc_Money(cost,q,d,n,p ):
#     refund = ((q*0.25)+(d*0.1)+(n*0.05)+(p*0.01))-cost
#     if refund >= 0:
#         print(f"Here is your ${refund} in change")
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunnded.")
#         return False
