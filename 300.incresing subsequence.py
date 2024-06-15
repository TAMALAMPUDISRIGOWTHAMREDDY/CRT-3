def fun(i,j,nums):
    n=len(nums)
    if i==n and i!=j:
        return 0
    elif nums[i]>nums[j]:
        return 1+fun(i+1,j+1,nums)
    return fun(i+1,j,nums)

print(fun(0,-1,[10,8,7,14,12,13,18]))
