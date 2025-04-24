import menu

def what_would_you_like():
    while menu.turned_on:
        try:
            i = input('What would you like? \'E\'(Espresso) / \'C\'(Cappuccino) / \'L\'(Latte): ').lower()
            if i == 'e' or i == 'espresso':
                e = 'espresso'
                if check_if_enough_resources(e):
                    manage_change(e)
                    process_resources(e)
                    print('Here is your Espresso. Enjoy!')
            elif i == 'c' or i == 'cappuccino':
                c = 'cappuccino'
                if check_if_enough_resources(c):
                    manage_change(c)
                    process_resources(c)
                    print('Here is your Cappuccino. Enjoy!')

            elif i == 'l' or i == 'latte':
                l = 'latte'
                if check_if_enough_resources(l):
                    manage_change(l)
                    process_resources(l)
                    print('Here is your Latte. Enjoy!')

            elif i == 'off':
                menu.turned_on = False
            elif i == 'report':
                print(f'Water: {menu.resources['water']}mL\nMilk: {menu.resources['milk']}mL\nCoffee: {menu.resources['coffee']}g\nMoney: ${menu.resources['money']}')
            else:
                print('Incorrect input, please input a drink.')
        except ValueError:
            print('Incorrect input type.')
    print('The coffee machine is now turning off...')


def check_if_enough_resources(d):
    enough_resources = True
    for i in menu.MENU[d]['ingredients']:
        if menu.resources[i] < menu.MENU[d]['ingredients'][i]:
            print(f'Sorry, there is not enough {i}.')
            enough_resources = False
    if not enough_resources:
        print('Call a manager to help you.')
    return enough_resources

def manage_change(d):
    print(f'The {d} costs: ${menu.MENU[d]['cost']}')
    paid = float(input('How much do you insert?'))
    if paid >= menu.MENU[d]['cost']:
        menu.resources['money'] += menu.MENU[d]['cost']
        change = round(paid, 2) - menu.MENU[d]['cost']

        q = int(change / 0.25)
        d = int((change % 0.25) / 0.1)
        n = int(((change % 0.25) % 0.1) / 0.05)
        p = int((((change % 0.25) % 0.1) % 0.05) / 0.01)
        print(f'Your change is ${change}: {q} quarters, {d} dimes, {n} nickels and {p} pennies.')

    else:
        print(f'{d} costs {menu.MENU[d]['cost']} but you only inserted {paid}. Money Refunded.')



def process_resources(d):
    for i in menu.MENU[d]['ingredients']:
        menu.resources[i] -= menu.MENU[d]['ingredients'][i]

what_would_you_like()
