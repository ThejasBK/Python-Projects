print('Welcome to ATM')
chances = 3
balance = 10000
restart = 'y'
while chances >= 0:
    pin = int(input('Enter your 4 digit pin: '))
    if pin == 3333:
        while restart == 'y':
            print('Press 1 for your balance')
            print('Press 2 for withdrawal')
            print('Press 3 to pay in')
            print('Press 4 to return card')
            option = int(input('Please enter your option: '))
            if option == 1:
                print('Youe balance is Rs. ',balance)
                restart = input('Do you want to go back?(y/n)')
                if restart == 'n':
                    print('Thank you')
                    break
            elif option == 2:
                withdrawal = float(input('Enter amount:'))
                if withdrawal > balance:
                    print('Not enough balance')
                else:
                    balance -= withdrawal
                print('Youe balance is Rs. ',balance)
                restart = input('Do you want to go back?(y/n)')
                if restart == 'n':
                    print('Thank you')
                    break
            elif option == 3:
                deposit = int(input('Enter the amount you\'re going to deposit: '))
                balance += deposit
                print('Youe balance is Rs. ',balance)
                restart = input('Do you want to go back?(y/n)')
                if restart == 'n':
                    print('Thank you')
                    break
            elif option == 4:
                print('Thank you for your service')
                break
            else:
                print('Incorrect option\nChoose the correct one')
    elif pin != 3333:
        print('Incorrect password')
        chances = chances - 1
        print('You\'ve got ',chances,' left')
        if chances == 0:
            print('You\'re card will be blocked \nContact the bank  for further details')
            break
