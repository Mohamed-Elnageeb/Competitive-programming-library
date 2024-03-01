mod = 10**9 + 7
def multiply(a, b):
    m = len(a)
    n = len(a[0])
    n2 = len(b[0])
    mul = [[0 for x in range(m)]
              for y in range(n2)]
    
    for i in range(m):
        for j in range(n):
            mul[i][j] = 0
            for k in range(n):
                mul[i][j] += a[i][k] * b[k][j]
                mul[i][j] %= mod
 
    # storing the multiplication
    # result in a[][]
    for i in range(m):
        for j in range(n):
            a[i][j] = mul[i][j]; # Updating our matrix
    return a
 
# Function to compute F raise
# to power n-2.
def matpower(m,n):
    if n%2 != 0 :
        return multiply(matpower(m,n-1),m)
    elif n > 0 :
        res = matpower(m,n//2)
        return multiply(res,res)
    else:
        identity = [[int(i==j) for j in range(len(m[0]))] for i in range(len(m))]
        return identity