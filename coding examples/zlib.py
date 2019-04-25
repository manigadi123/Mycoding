import zlib

s='hello world!hello world!helloworld!hello world!'
t=zlib.compress(s)
print t
print zlib.decompress(t)
