from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
turned_on = True

while turned_on:
    try:
        drink = menu.find_drink(input(f'What would you like? Available options: {menu.get_items()} ').lower())
        if drink == 'off':
            menu.turned_on = False
        elif drink == 'report':
            coffee_maker.report()
            money_machine.report()
        elif coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    except AttributeError:
        print('Incorrect input.')
print('The coffee machine is now turning off...')
