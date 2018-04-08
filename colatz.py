def collatz(num):
    # while num is not equal to 1
    while num != 1:
        #print num
        print(num)
        if num % 2 == 0:
            #if num is divisible by 2
            num = int(num / 2)
            # divide num by 2
        else:
            num = int(3 * num + 1)
            # else if it is odd multiple by 3 plus 1
    else:
        # once the number is eqaul to 1 print it and print done
        print(num)
        print('Done!')
# run the collaz method and iput the integer you want to run it on
def main():
    
    num = int(input('Input an integer: '))
    collatz(num)

main()
         
            


  
