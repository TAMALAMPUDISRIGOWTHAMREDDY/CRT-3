def printSum2(index, n, nums):
    if index == n:
        return nums[0]
    nextElementsSum = printSum2(index + 1, n, nums)#parent 
    return min(nextElementsSum,nums[index])        #child
 
nums = [12, 34, -12, 5, 7]
n = len(nums)
result = printSum2(0, n, nums)
print("min is:", result)


#parent to child 
'''def fun(i,n,list,mini):
    if i==n:
        return mini
    mini=min(mini,list[i])
    return fun(i+1,n,list,mini)  
    
list=[12,34,125,7]
n=len(list)
mini=list[0]
a=fun(0,n,list,mini)
print(a)'''
