
# Greatest common divisor of more than 2 numbers
def gcd(x,y): return y and gcd(y, x % y) or x  
#Lowest common multiple of 2 integers
def lcm(x,y): return x * y / gcd(x,y)  



# loops through number 1 to 20 and puts them  into the lcm fucntion to calculate the lowest common mulitple of 2 intergers
# Keeps looping until it getts to 20 and then you have the smallest number that can be divided by the numbers 1 to 20 
n = 1  
for i in range(1, 21):  
     n = lcm(n, i)  
print(n)  
