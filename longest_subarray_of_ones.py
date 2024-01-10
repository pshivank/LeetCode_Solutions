arr = list(map(int,input().split()))

k = 1
ans = []
for s in arr:
    if k == 0 and s == 0:
        break   
    elif s == 0 :
        k -= 1
        ans.append(s)
    else:
        ans.append(s)
        
if len(ans) < len(arr):   
    t = len(ans)
    n = t
    result = t
    
    for s in range(n,len(arr)):
        
        if arr[s] == 0 and ans[0] == 0 :
            ans.append(arr[s])
            ans.pop(0)
            
        elif arr[s] == 0 and ans[0] != 0 :
            
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
            
        result = max(result,t)
        
    print(result - 1)
    
else:
    print(len(ans) - 1)