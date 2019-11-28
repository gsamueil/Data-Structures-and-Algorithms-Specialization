#define  Recursion function take the index and return the number equivalent of that index 
def fib(index):
# if we not make any condition that will be infinite loop and make an error so we must make condition to stop the recursion 
#we have 0 and 1 not have and Fiboncci Numbers
   # if index==1:
       # return 1
  #  if index==0:
      #  return 0
    
    #we can use one if condtion 
    if index<=1:
        return index
    return fib(index-1)+fib(index-2)