import numpy as np

def selection_sort(x):
    for i in range(len(x)):
        swap=i+np.argmin(x[i:])
        x[i],x[swap]=(x[swap],x[i])
    return x
print selection_sort([23,23,221],[112,23,34],[121,23,34])
