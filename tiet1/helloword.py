import math;
def factorial(n):
    if(n == 1): 
        return 1
    else:
        return (n * factorial(n-1))
    
print("Nhập x: ")
x = float(input())
print("Nhập eps: ")
eps = float(input())
#bài1
mu = 1
first = 1
second = first + (x**mu) / factorial(mu)
    
while(math.fabs(first - second) > eps):
    mu+=1
    first = second
    second = first + (x**mu) / factorial(mu)
print(first)
			
#bài10
mu = 1
dau = 1
first = 0
second = first + dau * x**mu / mu
while (math.fabs(first - second) > eps):   
    mu += 2
    dau = -dau
    first = second
    second = first + dau * x**mu / mu
print(first)

def tichChan(n):
    rs = 1
    for i in range(1, n + 1) :
        if(i%2 == 0):
            rs = rs * i
    return rs
def tichLe(n):
    rs = 1
    for i in range(1, n + 1) :
        if(i%2 != 0):
            rs = rs * i
    return 

#bai2
mu = 1
dau = -1
first = 1
second = first + dau * ((mu+1) * (mu+2) / 2) * x**mu
while (math.fabs(first - second) > eps):
    mu = mu +1
    dau = - dau
    first = second
    second = first + dau * ((mu+1) * (mu+2) / 2) * x**mu
print(first)

#bai3
mu = 1
first = 0
second = - first - x**mu/ mu
while (math.fabs(first - second) > eps):
    mu = mu + 1
    first = second
    second = - first - x**mu / mu
print(first)

#bai 4
mu = 1
first = 1
dau = 1
second = first + dau * tichLe(mu * 2 - 2)/ tichChan(mu * 2) * x**mu
while (math.fabs(first-second) > eps):
    mu = mu + 1
    dau = -dau
    first = second
    second = first + dau * tichLe(mu * 2 - 2)/ tichChan(mu * 2) * x**mu
print(first)

# bai 5
mu = 1
first = 1
dau = -1
second = first + dau *tichLe(mu*2)/ tichChan(mu * 2) * x**mu
while (math.fabs(first-second)>eps):
    mu = mu + 1
    dau = -dau 
    first = second
    second = first + dau* tichLe(mu*2)/ tichChan(mu * 2) * x**mu
print(first)

#bai 6
mu = 1
dau = 1 
first = 0
second = first + dau * x**mu/ factorial(mu)
while (math.fabs(first - second) > eps):
    mu += 2
    dau = -dau
    first = second
    second = first + dau * x**mu / factorial(mu)
print(first)

#bai 7
mu = 2
dau = -1
first = 1
second = first + dau * x**mu / factorial(mu)
while (math.fabs(first - second) > eps):
    mu += 2
    dau = -dau
    first = second
    second = first + dau * x**mu / factorial(mu)
print(first)

#bai 8
mu = 3
first = x
second = first + tichLe(mu - 1) / tichChan(mu - 1) * x**mu / mu
while(math.fabs(first - second) > eps):
    mu += 2 
    first = second
    second = first + tichLe(mu - 1) / tichChan(mu - 1) * x**mu / mu
print(first)

#bai9
mu = 2
dau = -1
first = 1
second = first + dau * x**mu / factorial(mu+1)
while (math.fabs(first - second) > eps):
    mu += 2
    first = second
    dau = -dau
    second = first + dau * x**mu / factorial(mu+1)
print(first)

#bai 11
mu = 1
dau = 1
first = 0
second = first + dau * x**mu / mu
while (math.fabs(first - second) > eps):
    mu = mu + 1
    dau = -dau
    first = second
    second = first + dau * x**mu / mu
print(first)

#bai 12
first = 1
mu = 1
second = 2 * (first * (mu + 2 ) * x**mu / mu)
while (math.fabs(first - second) > eps):
    mu += 2
    first = second
    second = 2 * (first * (mu + 2 ) * x**mu / mu)
print(first)

#bai 13
mu = 1
first = 0
second = first + x**mu / factorial(mu)
while (math.fabs(first - second) > eps):
    mu += 2
    first = second
    second = first + x**mu / factorial(mu)
print(first)

#bai 14
mu = 2
first = 1
second = first + x**mu / factorial(mu)
while (math.fabs(first - second) > eps): 
    mu += 2
    first = second
    second = first + x**mu / factorial(mu)
print(first)

