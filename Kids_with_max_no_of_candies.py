arr = list(map(int,input().split()))
extra = int(input())
m = max(arr)
n = m - extra
ans = [False]*len(arr)

for s in range(len(arr)):
    if  arr[s] >= n :
        ans[s] = True
        
print(ans)