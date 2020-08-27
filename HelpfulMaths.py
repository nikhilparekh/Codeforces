a = input()
count = 0
temp = []
for i in a:
    if i.isnumeric():
        temp.append(i)
    else:
        count+=1
temp = sorted(temp)
plc = 1
while(count):
    temp.insert(plc,'+')
    plc+=2
    count-=1

temp = "".join(temp)
print(temp)