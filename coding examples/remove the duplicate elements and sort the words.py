s=raw_input("ENter the string:")
words = [word for word in s.split(" ")]
print words
l= " ".join(sorted(list(set(words))))
print l
