a='Python is a case sensitive language'
b=len(a)
c=a[::-1]
print(c)
d=a[10:-8]
print(d)
print(a.index("a"))
print(a[0:10],'object oriented',a[-8:])
for i in range (0,len(a)):
    if a[i]=='a':
        print(i)

e=a.replace(" ",'')
print(e)

    
