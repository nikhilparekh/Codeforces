arr = [1,2,3,4,9,8,6]
arr = sorted(arr)
hi = len(arr)-1
lo = 0
num = 1
while(lo<=hi):
    mid = lo+(hi-lo)//2
    if(arr[mid]==num):
        print(mid)
        break
    elif(arr[mid]>num):
        hi=mid-1
    else:
        lo=mid+1
