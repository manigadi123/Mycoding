# Suppose the following inputs are given to the program is 3,5

#then the output of the program should be
#[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]

# write a program which takes 2 digits x,y as input and generate a 2 dimensional arra y
# the element value in the ith row and jth  column of the array should be i*j


input_str=raw_input("enter the values:")
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]

multilist=[[0 for col in range(colNum) for row in range(rowNum)]]
print multilist

for row in range(rowNum):
    for col  in range(colNum):
        multilist[row][col]=row*col

print multilist
