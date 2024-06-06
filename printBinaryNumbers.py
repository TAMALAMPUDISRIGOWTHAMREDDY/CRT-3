'''def printBinaryNumbers(size, result, n):
    count=0
    if size == n:
        for i in result:
            if i=='(':
                count+=1
        if count==n/2 and result[0]=="(" and result[-1]==")":
            print(result)
        return 
    printBinaryNumbers(size + 1, result + '(', n)
    printBinaryNumbers(size + 1, result + ')', n)
n = 4
printBinaryNumbers(0, '', n)'''



# def par(size,res,n,n1,n2):
#     if n2>n1:
#         return
#     if n%2!=0:
#         print("Not possible")
#         return
#     if size==n:
#         if n1==n2 and res[0]=='(' and res[-1]==")":
#             print(res)
#         return
#     par(size+1,res+"(",n,n1+1,n2)
#     if n2>n1:
#         return
#     par(size+1,res+")",n,n1,n2+1)

# n=int(input())
# par(0,"",n,0,0)


def printThis(n, result, openOnes, closedOnes):
    if closedOnes > openOnes:
        return
    if openOnes > (n // 2) or closedOnes > (n // 2):
        return
    if len(result) == n:
        print(result)
        return 
 
    printThis(n, result + "(", openOnes + 1, closedOnes)
    printThis(n, result + ")", openOnes, closedOnes + 1)
 
 
n = 6
printThis(n, "", 0, 0)
