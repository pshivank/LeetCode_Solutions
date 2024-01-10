arr = list(map(int,input().split(',')))
k = int(input())
i = 0 
j = k 
max_avg = float('-inf') 
while j <= len(arr):
    if max_avg < (sum(arr[i:j]))/k:
        max_avg = (sum(arr[i:j]))/k
        i += 1
        j += 1
        
    else:
        i += 1
        j += 1
    
print(max_avg)
print(len(arr))

        
    