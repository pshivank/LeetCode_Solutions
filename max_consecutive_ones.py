arr = list(map(int,input().split()))
k = int(input())
ans = []
for s in arr:
    if k == 0 :
        break
    
    elif s == 0 :
        k -= 1
        ans.append(s)
        
    else:
        ans.append(s)
        
t = len(ans)
count = t

for s in range(len(ans),len(arr)):
    if arr[s] == 0 and ans[0] == 0 :
        ans.append(arr[s])
        ans.pop(0)
        
    elif arr[s] == 0 and ans[0] == 1:
        while True:
            ans.pop(0)
            t -= 1
            
            if ans[0] == 0 :
                break
            
        ans.append(arr[s])
        ans.pop(0)
        
    else:
        ans.append(arr[s])
        t += 1
        
    count = max(count,t)
    
print(count)

        
    
    
        
        