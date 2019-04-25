import zlib
s= 'hello world!hello world!hello wprd!'
t=zlib.compress(s)
print t
print zlib.decompress(t)
