test_str="MANI ekkada unnav i ma waiting for you from last 2 days"
d={}
for i in test_str:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print ("Count of all characters in GeeksforGeeks is :\n "
                                        +  str(d))
