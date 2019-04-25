import math
def binary_search(l,element):
    bottom=0
    top=len(l)-1
    index=-1
    while top>=bottom and index==-1:
        mid=int(math.floor(top+bottom)/2.0)
        if l[mid]==element:
            index=mid
        elif l[mid]>element:
            top=mid-1
        else:
            bottom=mid+1
        return index

l=[2,5,7,9,11,17,22,6364,3232,244,24325,2435,435,2435,2,4352,2535,535]
print binary_search(l,11)
print binary_search(l,22)
