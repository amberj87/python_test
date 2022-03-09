import math

def f(x,n):
    su=0
    term=1
    for i in range(1,n+1):
        su=su+term
        term=term*x/i
    su=su+term
    return(su)

print(f(3,500))