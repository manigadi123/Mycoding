nums=[1,2,3,4,5,6,7]
def genfun(nums):
    for n in nums:
        yield n*n
my_gen=genfun(nums)
for i in my_gen:
    print i
#print(genfun([1,2,2,3,4,5,5]))

my_gen=(n*n for n in nums)
print nums
type(nums)
print(type(my_gen))
