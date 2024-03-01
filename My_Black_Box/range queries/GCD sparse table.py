from math import ceil,log2,gcd

def rmq1(i,k) :

    # k = min(k,n-i) 

    ans = G[i][0] 
    # while k > 0 : 
        
    h = int(log2(k))  
    
    if G[i][h] != 0 : 
        ans = G[i][h]
    else:
        h3 = 1<<(h-1)
        ans = gcd(G[i][h-1],G[i+h3][h-1])
        
    return ans 


def rmq2(i,k) :

    h = int(log2(k)) 
    h2 = 1<<h
    
    if h2 == k : 
        return G[i][h] 
    else:
        r = i+k - h2
        return gcd(G[i][h],G[r][h])
        
arr = [1,2,3]
n = len(arr)  
lo = ceil(log2(n))+ 1

G = [[0 for i in range(lo)] for j in range(n)]

for i in range(n) : 
    G[i][0] = arr[i]

for i in range(lo) : 
    b = 1<<i 
    for j in range(n) : 
        if j+b > n : 
            break
        G[j][i] = rmq1(j,b) 