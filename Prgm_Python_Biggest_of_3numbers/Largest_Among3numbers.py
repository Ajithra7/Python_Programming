num1=float(input("enter the value of num1:"))
num2=float(input("enter the value of num2:"))
num3=float(input("enter the value of num3:"))
    
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)