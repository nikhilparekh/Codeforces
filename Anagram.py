st = 'Public relations'
temp = 'crap built on lies'
st = st.replace(' ','')
temp = temp.replace(' ','')
st = st.lower()
temp = temp.lower()
a = {}
b = {}
for i in st:
    a[i] = st.count(i)
for i in temp:
    b[i] = temp.count(i)


if(a==b):
    print("It is an Anagram")
else:
    print("It is not an Anagram")