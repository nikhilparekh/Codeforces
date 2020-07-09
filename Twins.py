num = int(input())
coins = list(map(int,input().split()))

if(num==1):
    print(1)
elif(num==2 and coins[0]==coins[1]):
    print(2)
else:
    count =0
    x = 0
    y = sum(coins)
    
    coins = sorted(coins,reverse=True)
    while(x<=y):
        x+=coins[count]
        y-=coins[count]
        count+=1
    print(count)

