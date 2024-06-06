'''def vowels(a,b,count,index):
    if index==len(a):
        return count
    if a[index] in b:
        count+=1
    return vowels(a,b,count,index+1)
a=input()
b="AEIOUaeiou"
ans=vowels(a,b,0,0)
print(ans)'''


#child to parent 
def countVowelsWay2(word, index, n):
    if index == n:
        return 0 
    nextVowelsCount = countVowelsWay2(word, index + 1, n)
    vowels = "aeiouAEIOU"
    if word[index] in vowels:
        nextVowelsCount += 1 
    return nextVowelsCount
 
 
word = "abcdeefuigh"
result = countVowelsWay2(word, 0, len(word))
print("Vowels count is:", result)

