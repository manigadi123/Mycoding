def sumOfTwo(l,n):
    count=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]== n:
                count+=1

    return count

print sumOfTwo([1,2,3,4,5,6,7,8,9],10)
                
