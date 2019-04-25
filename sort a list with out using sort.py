s=[1,'3','mani',25,"manjs","baaal",67,98,23]

for i in range(len(s)):
    for j in range(len(s)-1):
        if s[j]>s[j+1]:
            s[j],s[j+1]=s[j+1],s[j]
print s
