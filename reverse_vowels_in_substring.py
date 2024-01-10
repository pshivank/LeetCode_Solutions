string = input()
vowels = 'aeiouAEIOU'
avl_vowels = ''

for s in string:
    if s in vowels:
        avl_vowels += s
        
rev_vowels = avl_vowels[::-1]

i = 0
ans = ''
for s in range(len(string)):
    if string[s] in vowels:
        ans+=rev_vowels[i]
        i += 1 
    else:
        ans += string[s]

print(ans)
