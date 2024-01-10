arr = list(map(int,input().split()))
n = len(arr)

for s in range(n):
    if arr[s] == 0 :
        arr.remove(arr[s])
        arr.append(0)
        
print(arr)