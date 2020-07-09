s1 = "hello"
s2 = input()
count=0
for i in s2:
    if(count<=4 and i==s1[count]):
        count+=1
if(count==5):
    print("YES")
else:
    print("NO")
