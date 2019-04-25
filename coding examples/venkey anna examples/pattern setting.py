#input:["sachin cricket","Federer tennis","nadal tennins","virat cricket","messi football"]
#outpu:{"cricket":["sachin","cricket"],"tennis":["federer","nadal"],"football":["messi"]}



from collections import defaultdict

d = defaultdict(list)
l = ["sachin cricket","Federer tennis","nadal tennis","virat cricket","messi football"]
m={}
for i in l:
    if len(l[i])>14:
        key = "".join(i[-7:])
        d[key]="".join(i[0:6])
    else:
        key = "".join(i[-6:])
        d[key]="".join(i[0:6])
print d
t=set(d)
print t
     

