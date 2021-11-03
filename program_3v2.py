# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

def getMoney():
    return int(input('Amount of money: '))
    
def getPrice():
    return int(input('Price per apple: '))

def maxApple(_money,_price):
    _maxApple = _money//_price
    change = _money-_maxApple*_price
    print(f'You can buy {_maxApple} apples and your change is {change} pesos.')

money = getMoney()
price = getPrice()
appleM = maxApple(money,price)
