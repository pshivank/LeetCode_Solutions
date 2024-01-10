string = input()
k = int(input())
count = 0 
vowels = 'aeiou'
ans = ''
for s in range(k,len(string)+1):
    ans = string[s-k:s]
    temp = 0 
    for a in ans :
        if a in vowels :
            temp += 1 
            
            
    count = max(count,temp)
    print(ans)
    
    
    
print(count)
        


# optimized approach 

s = input()
k = int(input())
vowels = 'aeiou'
t = 0
string = s[:k]
for i in string :
    if i in vowels:
        t += 1
ans = t

for i in range(k,len(s)):
    if s[i] in vowels:
        t += 1
        
    if s[i-k] in vowels:
        t -= 1
        
    ans = max(ans,t)
    
print(ans)
