s=raw_input()
words=[word for word in s.split(" ")]
t=" ".join(sorted(list(set(words))))
print t
