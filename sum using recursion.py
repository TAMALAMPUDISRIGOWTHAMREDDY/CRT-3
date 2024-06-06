
#parent to child=================backtracking
'''def fun(i,n,list,sum):
    if i==n:
        return sum
    sum+=list[i]
    return fun(i+1,n,list,sum)
    
    
list=[1,3,4,6,7]
n=len(list)
sum=0
a=fun(0,n,list,sum)
print(a)'''


#child to parent =========================dynamic programming
def printSum2(index, n, nums):
    if index == n:
        return 0 
    nextElementsSum = printSum2(index + 1, n, nums)#parent 
    return nextElementsSum + nums[index]        #child
 
nums = [12, 34, 12, 5, 7]
n = len(nums)
result = printSum2(0, n, nums)
print("Sum is:", result)
