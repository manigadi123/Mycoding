a="""i am mani
i am  trainer
working developer"""

print a

#b=("i am big of powerstar"
   #"very good person in the world"
   #"best videos in mok")
#print b


c="it \nis \nprogramming \nlanguage"
print c

a=a.split('\n')
b=''
for each in a:
    each=each.split()
    for i in each:
        b+=i[-1]+i[:-1]+'ah'
        b+= '\n'

        print b
