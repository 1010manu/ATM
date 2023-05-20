import time
print('please insert your card')
time.sleep(2)
password=1999
pin=int(input('enter your atm pin'))
balance=10000
if pin==password:
    while True:
        print("""
            1.balance
            2.withdraw balance
            3.deposit balance
            4.exit
            """)
        try:
            option=int(input('please enter your choice'))
        except:
            print('please enter vaild option')
        if option==1:
            print(f'your current balance is {balance}')
        if option==2:
            withdraw=int(input('please enter amount'))
            balance=balance-withdraw
            print(f'{withdraw} is debited from your account')
            print(f'your current balance is {balance}')
        if option==3:
            deposit=int(input('please enter amount'))
            balance=balance+deposit
            print(f'{deposit} is credited to your account')
            print(f'your updated balance is {balance}')
        if option==4:
            print('thank you')
            break
    
else:
    print('wrong pin please try again')
        
        
        
        
        
