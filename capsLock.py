s = input()
if(s.isupper()):
    print(s.lower())
elif(s.islower() and len(s)==1):
    print(s.capitalize())
elif(s[0].islower() and s[1:].isupper()):
    print(s.capitalize())
else:
    print(s)
