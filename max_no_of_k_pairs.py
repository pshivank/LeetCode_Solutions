arr = list(map(int,input().split()))
k = int(input())
i = 0 
j = len(arr) - 1
count = 0 

arr.sort()

while i < j :
    if arr[i] + arr[j] == k :
        count += 1 
        i += 1
        j -= 1
        
    elif arr[i] + arr[j] > k :
        j -= 1
        
    else:
        i += 1
        
print(count)