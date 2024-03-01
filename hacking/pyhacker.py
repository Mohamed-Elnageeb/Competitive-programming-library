t = 2
from random import *
print(t)
mx = 10**9
seed(9) 
for i in range(t):
    n = 10**5
    print(n)
    cur = 0
    arr = [] 
    a = mx
    for i in range(1,n+1):
        # c20 : 172933
        # c17 : 107897
        # c14 : 62233
        #  126271 1056323 
        # a = max(1,(62233*i)%mx)
        a = randint(1,10**9)%(mx) + 1
        arr.append(a)
    # arr.append(1)
    arr.sort(reverse=1)
    print(*arr)
    # arr.reverse() 
    q = 2*10**5
    # print(q) 
    
    
    # for i in range(q) : 
    #     i = randint(0,n-1) 
    #     j = randint(0,n-1)
    #     if i == j : 
    #         j += 1
    #         j %= n 
    #     lst = [1+arr[j]%n,1+arr[i]%n ]
    #     lst.sort()
    #     print(*lst)