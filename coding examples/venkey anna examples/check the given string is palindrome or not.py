# function which return reverse of a string 
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    # Calling reverse function 
    rev = reverse(s) 
  
    # Checking if both string are equal or not 
    if (s == rev): 
        return True
    return False
  
  
# Driver code 
s = "malayalam"
ans = isPalindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No")


def isPalindrome(str):
    for i in xrange(0,len(str)/2):
        if str[i]!=str[len(str)-i-1]:
            return False
    return True
s="malayalam"


ans=isPalindrome(s)

if (ans):
    print("yes")
else:
    print "NO"
