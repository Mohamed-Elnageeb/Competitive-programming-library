from math import ceil,log2
def rmq1(i,k) :

    # k = min(k,n-i) 

    ans = mx[i][0] 
    # while k > 0 : 
        
    h = int(log2(k))  

    if mx[i][h] != 0 : 
        ans = mx[i][h]
    else:
        h3 = 1<<(h-1)
        ans = max(mx[i][h-1],mx[i+h3][h-1])
        
    return ans 

def rmq2(i,k) :

    ans = mn[i][0] 

    h = int(log2(k))  
    

    if mn[i][h] != 0 : 
        ans = mn[i][h]
    else:
        h3 = 1<<(h-1)
        ans = min(ans,mn[i][h-1],mn[i+h3][h-1])
    
    return ans 

def rmq3(i,k,g) :

    h = int(log2(k)) 
    h2 = 1<<h
    
    if g : 
        if h2 == k : 
            return mx[i][h] 
        else:
            r = i+k - h2
            return max(mx[i][h],mx[r][h])
    else:
        if h2 == k : 
            return mn[i][h] 
        else:
            r = i+k - h2 
            return min(mn[i][h],mn[r][h])
        
arr = [1,2,3]
n = len(arr)  
lo = ceil(log2(n+1)) 

mx = [[0 for i in range(lo)] for j in range(n)]
mn = [[0 for i in range(lo)] for j in range(n)]

for i in range(n) : 
    mx[i][0] = arr[i]
    mn[i][0] = arr[i]  

for i in range(lo) : 
    b = 1<<i 
    for j in range(n) : 
        if j+b > n : 
            break
        mx[j][i] = rmq1(j,b) 
        mn[j][i] = rmq2(j,b)  