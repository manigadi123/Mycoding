def count_range_in_list(li,min,max):
    ctr=0
    for x in li:
        if min<=x<=max:
            ctr+=1
    return ctr
li=[1,1,10,10,20,20,20,40,240]
print(count_range_in_list(li,1,240))

l1=['a','b','c','d','e']
print(count_range_in_list(l1,'b','e'))

