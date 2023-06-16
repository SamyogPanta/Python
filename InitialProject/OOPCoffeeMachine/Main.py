from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# ordering = True

# coffeeMaker = CoffeeMaker()
# menu = Menu()
# menuItem= MenuItem()
# moneyMachine = MoneyMachine()

# while ordering:
#     order = input("What would you like? (espresso/latte/cappuccino): ")
#     order = order.lower()
#     if order == "report":
#         print(coffeeMaker.report())
#         print(moneyMachine.report())
#     elif order == "exit":
#         print("Thank you. Have a great day")
#         ordering = False
#     else:
#         drink = menu.find_drink(order)
#         if coffeeMaker.is_resource_sufficient(drink.ingredients):
#             payment = moneyMachine.process_coins()
#             if moneyMachine.make_payment(menuItem.cost):
#                 coffeeMaker.make_coffee(order)




money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
               coffee_maker.make_coffee(drink)


