def printList():
    l2=list()
    for i in range(1,21):
        l2.append(i**2)
    return l2[-5:]
print printList()
