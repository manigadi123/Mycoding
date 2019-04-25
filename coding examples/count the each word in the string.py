#input: "New to Python or choosing between python2 and python3 ? Read python2 or python3
#output: count no.of each word:

freq={}
line=raw_input("Enter the line :")
for word in line.split():
    freq[word]=freq.get(word,0)+1

words=freq.keys()
words.sort()

for w in words:
    print "%s:%d" %(w,freq[w])
