st1 = input()
st2 = input()

ans = ''
l1 = len(st1)
l2 = len(st2)
m = min(l1,l2)
 
for s in range(m):
    ans += st1[s]
    ans += st2[s]
    
ans += st1[l2:] if l1 > l2 else st2[l1:]

print(ans)