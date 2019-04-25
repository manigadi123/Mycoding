v=['a','b','c','d','mani','ka']
p=''.join(v)
print p

# find the index of element in list

l=[1,2,4,5,6]
print l.index(4)

#shallow list

import itertools

p=[[1,2,3],[1,4,4],[3,3,2],[2,3,4]]
m=list(itertools.chain(*p))
print m

#append a list to second list

n=[12,2,3,0]
o=['red','green','black']
final=n+o
print final

#select an item randomly from list.

import random

color_list=['red','yellow','blue','whiote','pnnk']
print(random.choice(color_list))
