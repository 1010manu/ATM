print('welcome to sbi')
trys=3
userpin=1999
while trys!=0:
    pin=int(input('enter 4 digit number:'))
    if pin!=userpin:
        trys-=1
        print(f"worng pin number, you have {trys} trys left")
        if trys==0:
            print('remove your card')
            break
    else:
        userchoice =input("""d:deposit
w:withdraw
""")
        if userchoice=='d':
            userdeposit=int(input('enter the amount:'))
            print(userdeposit,'$ have been deposited')
        if userchoice=='w':
            userwithdraw=int(input('enter the amount:'))
            print(userwithdraw,'$ have been withdrawed')
    userexit=input('would you like to continue? Y,N:')
    if userexit=='N' or  userexit=='n' :
        print('thank you for using')
        break
    elif userexit=='Y' or  userexit=='y':
        continue
    else:
        print('invalid')
        print('remove your card')
        break
        
        
    
