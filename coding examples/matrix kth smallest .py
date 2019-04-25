import heapq 
  
def kthSmallest(input): 
  
    # assign first row to result variable 
    # and convert it into min heap 
    result = input[0]  
    heapq.heapify(result) 
  
    # now traverse remaining rows and push 
    # elements in min heap 
    for row in input[1:]: 
         for ele in row: 
              heapq.heappush(result,ele) 
  
    # get list of first k smallest element because 
    # nsmallest(k,list) method returns first k  
    # smallest element now print last element of  
    # that list 
    kSmallest = heapq.nsmallest(k,result) 
    print (k,"th smallest element is ",kSmallest[-1]) 
  
# Driver program 
if __name__ == "__main__": 
    input = [[10, 25, 20, 40], 
           [15, 45, 35, 30], 
           [24, 29, 37, 48], 
           [32, 33, 39, 50]] 
    k = 2
    kthSmallest(input)
