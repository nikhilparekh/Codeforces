a = input()

def answer(a):
    count = 1
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            count+=1
        else:
            count=1
        if(count>6):
            print("YES")
            return
    print("NO")

answer(a)