string = input()
new = string.split(' ')
ans = ''
space = ' ' * 100000
for s in range(len(new)-1 , -1 , -1):
    if new[s] not in space:
        ans += new[s]
        ans += ' '
    
print(ans)