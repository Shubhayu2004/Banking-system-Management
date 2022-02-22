is_logined = False
is_quit = False

user = {
    'name': '',
    'balance': 0
}

def new_user():
    name = input('Enter your name: ')
    user['name'] = name
    global is_logined
    is_logined = True

def withdraw_money():
    try:
        w_amount = int(input('How much money you want to withdraw : '))
        if w_amount > user['balance']:
            print('Insufficient balance . Your current balance is '+ user['balance'] )
        else:
            user['balance'] = user['balance'] - w_amount
            print(f'{w_amount} has been withrawn from your account your total balance left is {user["balance"]}')
            print('')
    except:
        print('Please enter a number')

def deposit_money():
    try:
        d_amount = int(input('How much money you want to deposit : '))
        user['balance'] = user['balance'] + d_amount
        print(f'{d_amount} has been deposited to your account your total balance is {user["balance"]}')
        print('')
    except:
        print('Please enter a number')

def show_balance():
    print(f'Your balance is {user["balance"]}')
    print('')

def start():
    while is_quit == False:
        if is_logined == False:
            print('Create your account : ')
            new_user()
        else :
            print(f'Welcome to bank {user["name"]} what you want to do ')
            res = input('Press w for withdraw and d to deposit and b to show your balance and q to exit: ')
            if res == 'w':
                withdraw_money()
            elif res == 'd':
                deposit_money()
            elif res == 'b':
                show_balance()
            elif res == 'help':
                print('Press w for withdrawing money')
                print('Press d for depositing money')
                print('Press b for showing your balance')
                print('Press q for showing quiting the program')
            elif res == 'q':
                break
            else:
                print('Enter a correct value from given type help for commands')

start()