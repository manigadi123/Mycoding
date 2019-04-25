def sub_list(my_list):
    subs=[[]]
    for i in range(len(my_list)):
        n=i+1
        while n<=len(my_list):
            sub=my_list[i:n]
            subs.append(sub)
            n+=1

    return subs
l1=[1,2,3,4,5,6,6,6,6,4,3,2,87]
l2=['a','b','c','c','d','e']

print sub_list(l1)
#print sub_list(l2)
