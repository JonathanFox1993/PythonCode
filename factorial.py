
#So this function will keep looping until the integer n is equal to 1
#Each time it will multiply the num which starts as 1 by the number you enter and put num equal to that ammount 
#then it reduces the number you put in by 1 and does this until the number you entered is down to one 1
#Num will keep getiing muliplied until it gets the factorial
#it then prints out the factorial
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    print (num)

def main():
    num = int(input('Input an integer: '))
    factorial(num)

main()
