a=int(input())
b=int(input())
c=int(input())

if a>b:
    max=a
    if a>c:
        max=a
    else:
        max=c
elif b>a:
    max =b
    if b>c:
        max=b
    else:
        max=c

print(max)
        
