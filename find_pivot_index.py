nums = list(map(int,input().split()))

pivot_index = 0
left_sum = 0 
right_sum = sum(nums[pivot_index+1:])

while pivot_index < len(nums):
    if left_sum == right_sum:
        break
                
    else:
        pivot_index += 1
        left_sum = sum(nums[:pivot_index])
        right_sum = sum(nums[pivot_index + 1 :])
                
            
                
if pivot_index == len(nums):
    pivot_index = -1
            
print(pivot_index)