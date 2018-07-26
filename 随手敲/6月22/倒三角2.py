n=10
while n>0:
    n=n-1
    s='*'*n
    if n%2==1:
        print(s.center(10))
    
for i in range(10,0,-1):
    if i%2==1:
        s='*'*i
        print(s.center(10))
