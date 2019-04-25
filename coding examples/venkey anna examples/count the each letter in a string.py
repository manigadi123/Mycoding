#count the each letter in the string:
test_str="Mani is a good boy"
d={}
for i in test_str:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print("The no.of occurances of each letter is :\n" +str(d))


def countfreq(test_str):
    d={}
    for i in test_str:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
print countfreq("Mani is a good boy")
