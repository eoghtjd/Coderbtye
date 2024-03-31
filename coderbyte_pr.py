def insert_card():
    print('Card inserted')
    return True  

def pin(pin):
    if pin == '2024':
        print('PIN entered')
        return True  
    else:
        print('Invalid PIN')
        return False  

def atm(op, balance):
    if op == "1":
        print("Balance:", balance)

    elif op == "2":
        deposit = int(input('Deposit amount (No cents): '))
        balance += deposit  
        print(f"Balance updated: {balance}")

    elif op == "3":
        withdraw = int(input('Withdraw amount: '))
        if balance - withdraw < 0:
            print('Not enough balance')
        else:
            balance -= withdraw
            print(f'Take {withdraw}')
            print(f"Balance updated: {balance}")
    
    return balance 


if insert_card():
    pin_number = input("Enter PIN: ")
    if pin(pin_number):
       
        account1_balance = 1500
        account2_balance = 2000
        
        
        while True:
            account_choice = input("Choose account: 1 or 2: ")
            if account_choice not in ['1', '2']:
                print("Invalid account choice. Please select 1 or 2.")
            else:
                break
        
       
        if account_choice == '1':
            while True:
                op = input("Press 1 = See Balance, 2 = Deposit, 3 = Withdraw, 4 = Exit: ")
                if op == '4':
                    break
                account1_balance = atm(op, account1_balance)  
        elif account_choice == '2':
            while True:
                op = input("Press 1 = See Balance, 2 = Deposit, 3 = Withdraw, 4 = Exit: ")
                if op == '4':
                    break
                account2_balance = atm(op, account2_balance)  
