# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

def getpriceApple():
    return 20

def getpriceOrange():
    return 25

def getApples():
    return int(input('Number of apples (20 pesos each): '))

def getOranges():
    return int(input('Number of oranges (25 pesos each): '))

def totalAmount(appleF,orangeF,pApple,pOrange):
    _total = (appleF*pApple + orangeF*pOrange)
    print(f'The total amount is {_total} pesos.')

applePrice = getpriceApple()
orangePrice = getpriceOrange()
apple = getApples()
orange = getOranges()
total =  totalAmount(apple,orange,applePrice,orangePrice)