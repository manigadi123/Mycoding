import sys
netAmount=0
while True:
    s=raw_input("enter the amount :")
    if not s:
        break
    values=s.split(" ")
    operation=values[0]
    amount=int(values[1])
    if operation=="D":
        netamount+=amount
    elif operation=="W":
        netamount-=amount
    else:
        pass
print netAmount
