def second_smallest(num):
    a1=a2=float('inf')
    for x in num:
        if x<=a1:
            a1,a2=x,a1
        elif x<a2:
            a2=x
    return a2
print(second_smallest([1,2,3,-8,-2,0]))

# find second largest number
def second_largest(num):
    count=0
    n1=n2=float('-inf')
    for x in num:
        count +=1
        if x>n2:
            if x>n1:
                n1,n2=x,n1
        else:
            n2=x
    return n2 if count>=2 else None
print(second_largest([1,2,3,-9,0,32]))
            
        
