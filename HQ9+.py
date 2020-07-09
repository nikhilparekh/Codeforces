s = input()
flag = 1
for i in s:
    if(i=='+'):
        pass
    elif(i=="H" or i=="Q" or i =="9"):
        print("Yes")
        flag = 0
        break
if(flag):
    print("NO")