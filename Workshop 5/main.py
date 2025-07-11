# Input
while True: 
    print('1.Buy')
    print('2.Sell')
    print('3.Exit')
    try:
        a = int(input('Enter a buy and sell product: '))
        if a == 1:
            print('Buy product')
        elif a == 2:
            print('Sell product')
        elif a == 3:
            print('Exit the product')
            break
        else:
            print("Invalid.")
    except ValueError:
        print("Enter a valid number.")