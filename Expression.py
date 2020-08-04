temp = []
for i in range(3):
    a = int(input())
    temp.append(a)
temp = sorted(temp)
res = 1

for i in range(len(temp)):
    if(temp[i]==1):
        temp[i+1]+=temp[i]
        temp.remove(temp[i])
    else:
        res*=i
print(res)