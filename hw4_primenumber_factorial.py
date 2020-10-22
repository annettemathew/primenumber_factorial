import cmath

#Display all the prime numbers within a range where start and
# end of the range is input by the user.
# (Example - prime numbers between 10 and 100)
#Find the factorial of any number
#Reverse a given integer number
#Example
#Given:
#76542
#Expected output:
#24567
#Print the following pattern

#prime number problem
lower = int(input("lower range: "))
upper = int(input("upper range: "))
if(upper < lower): #swap
    print("Incorrect input. will swap these numbers")
    temp = lower
    lower = upper
    upper = temp
list = []
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, int(cmath.sqrt(num).real)):
        #just need to go up till square root of number instead of up till the number itself
            if (num % i) == 0:
                print(num, " is not prime")
                break
        else:
            print(num, " is prime.")

#factorial
n = input("Enter a number: ")
def factorial(n):
    if(n == 1 or n == 0): #base case and 0 to avoid errors
        return 1
    elif(n < 1): #avoiding errors from negative numbers
        print("not applicable, will change to absolute value")
        n = abs(n)

    return n * factorial(n - 1)
print(factorial(int(n)))



#print reverse
num = int(input("Please enter a number you would like to reverse: "))
rev_num = 0
if(num < 0):
    print("I am switching negative numbers to positive")
    num = abs(num)
while(num > 0):
    rev_num = (rev_num * 10) + (num % 10)
    #multiplies by 10 to move the number one to the left
    # & adds the remainder of the mod to the ones place
    num = num // 10
    #uses floor division to only return the integer part of the number
print(rev_num)

#star pattern
for i in range(0, 4):
#for each number 0 thru 4
    for j in range(0, i + 1):
    #goes from 0 to one more than  the outer loop to add the extra star each time
        print("* ", end="")
    print("\r")
    #enter key
for i in range (4, 0, -1):
    #goes from 4 down to 0
    for j in range(0, i - 1):
    #goes from 0 to one less than the outer loop to subtract one star from each line
        print("* ", end='')

    print("\r")

