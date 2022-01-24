n = int(input("Sum of even numbers till "))

sum = 0
for i in range(1,n+1):
    if ((i%2)==0):

        sum = sum + i
       
    
print("The sum of even numbers ",sum)
