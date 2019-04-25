from collections import Counter 
  
def anagram(input1, input2): 
  
    # Counter() returns a dictionary data 
    # structure which contains characters  
    # of input as key and their frequencies 
    # as it's corresponding value 
    return Counter(input1) == Counter(input2) 
  
# Driver function 
if __name__ == "__main__": 
    input1 = 'abcdc'
    input2 = 'dcabc'
    print anagram(input1, input2) 
