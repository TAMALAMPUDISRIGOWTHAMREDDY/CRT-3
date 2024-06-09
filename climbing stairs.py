def fun(i,n):
    if i==n:
        return 1
    if i>n:
        return 0
    a=fun(i+1,n)
    b=fun(i+2,n)
    return a+b
print(fun(0,5))