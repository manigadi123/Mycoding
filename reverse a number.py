# Python Program to Reverse a Number using While loop    
     
Number = int(input("Please Enter any Number: "))    
Reverse = 0    
while(Number > 0):    #5>0
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder    
    Number = Number //10    
     
print("\n Reverse of entered number is = %d" %Reverse)

x=123
b=str(x)
print b
print b[::-1]

