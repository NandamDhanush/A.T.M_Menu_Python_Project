accounts = {
    285639 : [3678, 'Name1', 100000, '7675861903'],
    947810 : [9845, 'Name2', 200000, '9877025556'],
    449167 : [4901, 'Name3', 156786, '7969754978']
}

boolean = True
while boolean:
    print('A.T.M Menu')
    print('Select the Required Option:')
    print('1 - Check Balance')
    print('2 - Deposit')
    print('3 - Withdraw')
    print('4 - Pin Change')
    print('5 - Pin Generation')
    print('6 - Exit')
    option = int(input('Select Option: '))
    if option == 1:
        accno = int(input('Enter your Account Number: '))
        if accno not in accounts:
            print('Account Does Not Exist! Please Try Again.')
        else:
            pin = int(input('Enter Your Pin: '))
            if pin == accounts[accno][0]:
                print(f'Available Balance: {accounts[accno][2]}')
            else:
                print('Incorrect Pin Number! Please Try Again.')
    elif option == 2:
        accno = int(input('Enter your Account Number: '))
        if accno not in accounts:
            print('Account Does Not Exist! Please Try Again.')
        else:
            pin = int(input('Enter Your Pin: '))
            if pin == accounts[accno][0]:
                daccno = int(input("Please Enter the Account Number where you'd like to Deposit Money: "))
                if daccno not in accounts:
                    print('Account Does Not Exist! Please Try Again.')
                else:
                    dmoney = int(input(f"Enter the Amount you'd like to Deposit into Account Number {daccno}: "))
                    accounts[daccno][2] += dmoney
                    print(f'Successfully Added {dmoney}')
            else:
                print('Incorrect Pin Number! Please Try Again.')
    elif option == 3:
        accno = int(input('Enter your Account Number: '))
        if accno not in accounts:
            print('Account Does Not Exist! Please Try Again.')
        else:
            pin = int(input('Enter Your Pin: '))
            if pin == accounts[accno][0]:
                wmoney = int(input("Please Enter the Amount you'd like to Withdraw: "))
                if wmoney > accounts[accno][2]:
                    print('Insufficient Funds! Please Try Again.')
                    print(f'Available Balance: {accounts[accno][2]}')
                else:
                    accounts[accno][2] -= wmoney
                    print('Collect your Cash')
                    print(f'Money Debited Successfully - {wmoney}')
                    print(f'Current Balance: {accounts[accno][2]}')
            else:
                print('Incorrect Pin Number! Please Try Again.')
    elif option == 4:
        accno = int(input('Enter your Account Number: '))
        if accno not in accounts:
            print('Account Does Not Exist! Please Try Again.')
        else:
            mobile = input('Enter Your Mobile Number: ')
            if mobile == accounts[accno][3]:
                pin = int(input('Enter Your Current Pin: '))
                if pin == accounts[accno][0]:
                    npin = int(input('Enter your New Pin: '))
                    cpin = int(input('Re Enter your New Pin: '))
                    if npin == cpin:
                        accounts[accno][0] = npin
                        print('Pin Changed Succesfully')
                    else:
                        print('Pin not Entered correctly! Please Try again')
                else:
                    print('Incorrect Pin Number! Please Try Again')
            else:
                print('Check Your Mobile Number! and Try Again')
    elif option == 5:
        print('Hello User Welcome!')
        accno = int(input('Enter your Account Number: '))
        if accno in accounts:
            print('Account Already Exist! Please Try Again')
        else:
            name = input('Enter Your Name: ')
            mobile = input('Enter your Mobile Number: ')
            npin = int(input('Enter your New Pin: '))
            cpin = int(input('Re Enter your New Pin: '))
            if npin == cpin:
                accounts[accno] = [cpin, name, 0, mobile]
                print('Pin Generation Succesfully')
            else:
                print('Pin Generation Unsuccesfully')
    else:
        print('Thanks for Choosing Us (:')
        boolean = False
    
