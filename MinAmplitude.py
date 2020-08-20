A = [1,2,3,4,5]

def sub(A,k):
    cur = res = A[0:k]
    for i in range(1,len(A)):
        cur = A[i:i+k]
        a = sum(cur)
        b = sum(res)
        if(a>b):
            res = cur
    return res

print(sub(A,9))