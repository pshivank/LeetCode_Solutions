def isPalindrome(string):
    new = string[::-1]
    
    if string == new :
        return True 
    else:
        return False
    
def longest_pd_st(string):
    ans = string[-1]
    
    for s in range(len(string)-1):
        temp = string[s]
        for a in range(s+1 , len(string)):
            temp += string[a]
            if temp == temp[::-1] and len(temp) >= len(ans):
                ans = temp 
                
    print(ans)
    
def main():
    string = input()
    
    longest_pd_st(string)
    
if __name__ == '__main__':
    main()