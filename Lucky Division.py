num = int(input())

if(num%4==0 or num%7==0 or num%47==0):
    print("YES")
elif(num%10==4 or num%10==7):
    while(num%10==4 or num%10==7):
        num//=10
    if(num==0):
        print("YES")
    else:
        print("NO")
else:
    print("NO")


    

