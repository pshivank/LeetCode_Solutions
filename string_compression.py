chars = list(input().split())

i, k, n = 0, 0, len(chars)
while i < n:
    j = i + 1
    while j < n and chars[j] == chars[i]:
        j += 1
    chars[k] = chars[i]
    k += 1
    if j - i > 1:
        cnt = str(j - i)
        for c in cnt:
            chars[k] = c
            k += 1
    i = j
            
chars = chars[:k]
print(chars)
print(k)
print(i)