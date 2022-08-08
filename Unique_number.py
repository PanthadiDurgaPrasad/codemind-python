n=int(input())
l=[]
while n!=0:
    r=n%10
    l.append(r)
    n=n//10
g=len(l)
c=[]
for i in l:
    if i not in c:
        c.append(i)
if g==(len(c)):
    print("Unique Number")
else:
    print("Not Unique Number")