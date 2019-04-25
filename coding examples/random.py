import random

print random.random()*100
print random.random()*100-5
print random.choice([i for i in range(11) if i%2==0])
print random.choice([i for i in range(201) if i%5==0 and i%7!=0])
print random.sample(range(100),5)
print random.sample([i for i in range(1,201) if i%2==0], 5)
print random.sample([i for i in range(1,1001) if i%5==0 and i%7!=0], 10)
print random.randrange(7,16)

