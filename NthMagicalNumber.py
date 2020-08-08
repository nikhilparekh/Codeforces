x = 'nikhil'
y = 'iinkhl'
d = {}
t = {}
for i in x:
    d[i] = x.count(i)
for i in y:
    t[i] = y.count(i)
print(d==t)
c = list(x)
print(c)