s = "11:59"
s = s[:2]+s[3:]
temp = []
temp = sorted(s)
print(temp)

for i in temp:
    x = s[:3]
    x+=i
    if(x>s):
        print(x)
        break

    