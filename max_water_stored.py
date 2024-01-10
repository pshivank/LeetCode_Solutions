heights = list(map(int,input().split()))
i = 0 
j = len(heights)-1
si = 0 
ei = 0 
max_water = 0

while i < j :
    h = min(heights[i] , heights[j])
    w = j-i
    
    if max_water < h*w :
        max_water = h*w
        si = i 
        ei = j
        
    elif heights[i] < heights[j]:
        i += 1
    else:
        j -= 1
        
print(max_water)
print(si,ei)