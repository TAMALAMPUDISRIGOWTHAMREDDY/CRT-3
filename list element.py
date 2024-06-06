# def findSubsets(i,l,res):
#     if i==len(l):
#         print(res)
#         return
#     res.append(l[i])
#     findSubsets(i+1,l,res)
#     res.pop()
#     findSubsets(i+1,l,res)
# l=[1,2,3,4,5]
# res = []
# findSubsets(0,l,res)
 

# def prints(a,i,n,l):
#     if i == n:
#         print(l)
#         return
#     l.append(a[i])
#     prints(a,i+1,n,l)
#     l.pop()
#     prints(a,i+1,n,l)
# a = [1,5,4]
# prints(a,0,len(a),[])

# def generate(i, orig, curr):
#     if i == len(orig):
#         print(curr)
#         return
#     generate(i + 1, orig, curr+ [orig[i]])
#     generate(i + 1, orig, curr)
# orig=[1,2,4,5,6,7,9]
# generate (0,orig,[])

