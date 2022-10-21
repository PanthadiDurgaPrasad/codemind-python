def pal(x):
    s=0
    n=x
    while x!=0:
        r=x%10
        s=s*10+r
        x=x//10
    if s==n:
        return True
    else:
        return False
def npal(x):
    while pal(x)!=True:
        x+=1
    return x
def ppal(x):
    while pal(x)!=True:
        x-=1
    return x
x=int(input())
p=ppal(x)
n=npal(x)
if pal(x)==True:
    print(ppal(n-1),npal(p+1))
elif x-p<n-x:
    print(p)
elif x-p>n-x:
    print(n)
elif x-p==n-x:
    print(p,n)