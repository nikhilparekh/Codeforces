a = 'abcdea'
d = []

def uni(a):
    for i in a:
        if(i in d):
            return False
        else:
            d.append(i)
    return True

print(uni(a))
