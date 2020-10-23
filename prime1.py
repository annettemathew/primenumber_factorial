num1=int(input("Enter the starting point : "))
num2=int(input("Enter the ending point : "))
print("Prime number are: ")
for num in range(num1,num2+1):
    if num == 1 or num == 0:
        continue
    else:
        for j in range(2,num):
            if num%j==0:
                break
        else:
            print(num,end=' ')
