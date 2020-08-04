def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    temp = ''
    for i in range(len(s)):
        if(s[i].isalnum()):
            temp+=s[i]
    rev = temp[::-1]
    return rev==temp