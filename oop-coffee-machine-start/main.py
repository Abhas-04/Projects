from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffe_menu=Menu()
coffee_maker=CoffeeMaker()
money_machine= MoneyMachine()
is_on=True
option=coffe_menu.get_items()

while is_on:
 choice=input(f"What would you like to have? {option}:")
 if choice == "off":
     is_on = False
 elif choice == "report":
     coffee_maker.report()
     money_machine.report()
 else:
     drink=coffe_menu.find_drink(choice)
     if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
         coffee_maker.make_coffee(drink)





