#child to parent dynamic programming
'''def printSum2(index, n, nums):
    if index == n:
        return 0 
    nextElementsSum = printSum2(index + 1, n, nums)#parent 
    return max(nextElementsSum,nums[index])        #child
 
nums = [12, 34, 12, 5, 7]
n = len(nums)
result = printSum2(0, n, nums)
print("max is:", result)'''




#parent to child=================backtracking
def fun(i,n,list,maxi):
    if i==n:
        return maxi
    maxi=max(maxi,list[i])
    return fun(i+1,n,list,maxi)
    
    
list=[12,34,125,7]
n=len(list)
maxi=list[0]
a=fun(0,n,list,maxi)
print(a)
