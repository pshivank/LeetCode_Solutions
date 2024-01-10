arr = list(map(int,input().split()))
ans = [1]*len(arr)
for s in range(len(arr)):
    for a in range(len(arr)):
        if a != s :
            ans[s] *= arr[a] 
            
print(ans)
        

# optimized approach 


def count_zero(arr):
    zero = 0 
    n = 1
    for s in arr:
        if s == 0 :
            zero += 1
        else:
            n *= s
            
    return zero , n 

def product(arr):
    zero , n = count_zero(arr)
    ans = [0] * len(arr)
            
    if zero > 1 :
        return ans 
    
    elif zero == 1 :
        for s in range(len(arr)):
            if arr[s] == 0 :
                ans[s] = n
    
    else:
        for s in range(len(arr)):
            ans[s] = n // arr[s]
            
    return ans 
        

def main():
    arr = list(map(int,input().split()))
    zero , n  = count_zero(arr)
    print(zero,n)
    print(product(arr))
    
    
if __name__ == '__main__':
    main()
    