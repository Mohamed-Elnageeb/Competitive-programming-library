# ﷽
import sys
import heapq 
from heapq import *
from math import log2,ceil,floor,gcd,sqrt,log,perm,comb,factorial
from random import randrange
from bisect import bisect_left 
from collections import defaultdict, Counter, deque, OrderedDict
from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
from types import GeneratorType

input = lambda: sys.stdin.buffer.readline().decode().rstrip()



class dict_(dict):
    RANDOM = randrange(2 ** 62)
 
    def __init__(self, dd):
        super().__init__({k ^ self.RANDOM: v for k, v in dd.items()})
 
    def __missing__(self, key):
        return 0
 
    def __setitem__(self, key, value):
        super().__setitem__(key ^ self.RANDOM, value)
 
    def __getitem__(self, item):
        return super().__getitem__(item ^ self.RANDOM)
 
    def __contains__(self, item):
        return super().__contains__(item ^ self.RANDOM)
 
    def items(self):
        for k, v in super().items():
            yield (k ^ self.RANDOM, v)
 
    def keys(self):
        for k in super().keys():
            yield k ^ self.RANDOM
 
    def __repr__(self):
        return '{0}'.format({k ^ self.RANDOM: v for k, v in super().items()})

###############################################################################
# GRAPHS :

def add_edge(node1,node2,graph):

    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)
    graph[node2].append(node1)

class disjointset:
    def __init__(self, n):
        self.rank, self.parent = array('i', [0] * (n + 1)), array('i', [i for i in range(n + 1)])
        self.n, self.even = n, array('b', [0] * (n + 1))
 
    def find(self, x):
        xcopy = x
        while x != self.parent[x]: x = self.parent[x]
        while xcopy != x:
            self.parent[xcopy], xcopy = x, self.parent[xcopy]
        return x
 
    def union(self, x, y):
        xpar, ypar = self.find(x), self.find(y)
 
        if xpar == ypar: return 1
 
        par, child = xpar, ypar
        if self.rank[xpar] < self.rank[ypar]:
            par, child = ypar, xpar
 
        elif self.rank[xpar] == self.rank[ypar]:
            self.rank[xpar] += 1
 
        self.parent[child] = par
        self.even[par] |= self.even[child]
        self.n -= 1
        return 0


def dijkstra(graph, start1):
    distances = {node: float('inf') for node in graph}  # Initialize distances to infinity
    distances[start1] = 0  # Distance from start1 to start1 is 0
    heap = [(0, start1,[start1])]  # Priority queue to store nodes and their distances
    paths = [-1 for i in range(n+1)]
    while heap:
        current_distance, current_node , path = heapq.heappop(heap)  # Get node with smallest distance
        
        if current_distance > distances[current_node]:
            continue  # Skip if distance is already greater than the known distance

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight  # Calculate tentative distance

            if distance < distances[neighbor]:
                lst = path 
                lst.append(neighbor)
                paths[neighbor] = current_node
                distances[neighbor] = distance  # Update distance if shorter
                heapq.heappush(heap, (distance, neighbor, lst))  # Add neighbor to the heap

    return distances , paths



###############################################################################
def mergeSort(arr, n):
    # A temp_arr is created to store
    # sorted array in merge function
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n-1)
 
# This Function will use MergeSort to count inversions
 
 
def _mergeSort(arr, temp_arr, left, right):
 
    # A variable inv_count is used to store
    # inversion counts in each recursive call
 
    inv_count = 0
 
    # We will make a recursive call if and only if
    # we have more than one elements
 
    if left < right:
 
        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python
 
        mid = (left + right)//2
 
        # It will calculate inversion
        # counts in the left subarray
 
        inv_count += _mergeSort(arr, temp_arr,
                                left, mid)
 
        # It will calculate inversion
        # counts in right subarray
 
        inv_count += _mergeSort(arr, temp_arr,
                                mid + 1, right)
 
        # It will merge two subarrays in
        # a sorted subarray
 
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count
 
# This function will merge two subarrays
# in a single sorted subarray
 
 
def merge(arr, temp_arr, left, mid, right):
    i = left     # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0
 
    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.
 
    while i <= mid and j <= right:
 
        # There will be no inversion if arr[i] <= arr[j]
 
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
 
    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
 
    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
 
    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
 
    return inv_count
###############################################################################


def Divisors(n) :
    divisors = {}
    for num in [n]: 
        lst = set()
        i = 1
        while i <= sqrt(num):
            
            if (num % i == 0) :
                # If divisors are equal, print only one
                if ( num / i == i) :
                    lst.add(i)
                else :
                    # Otherwise print both
                    lst.update([i,num//i])
                
            i = i + 1
        divisors[num] = list(lst)
    return divisors[num]

def binpow(a, b):
    if b==0:
        return 1
    res = binpow(a,b//2)
    res = pow(res,2,MOD)
    if b%2:
        return (res*a)%MOD
    return res
 
def mod_inverse(a):
    return binpow(a,MOD-2)
 
def factors(n): 
    if n==0:
        return set()   
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
 
# factors = [factors(i) for i in range(MAX)]
 
# factorial and inverse factorial
 
# fact = [1]*MAX
# invfact = [1]*MAX
# for i in range(1,MAX):
#     fact[i] = (fact[i-1]*i)%MOD
#     invfact[i] = (invfact[i-1]*mod_inverse(i))%MOD

def inverse_mod(num):
    a = mod-2
    result = 1
    result=pow(num,a,mod)
    return result 

def mex(arr, N):
    # Sort the array
    arr1 = arr.copy()
    arr1.sort()
    mex = 0
    for idx in range(N):
        if arr1[idx] == mex:
            # Increment mex
            mex += 1
    # return mex as answer
    return mex
###############################################################################
    
def mergeDictionary(dict_1, dict_2):
   dict_3 = {**dict_1, **dict_2}
   for key, value in dict_3.items():
       if key in dict_1 and key in dict_2:
               dict_3[key] = value + dict_1[key]
   return dict_3
   
def rindex(lst, value):
    lst.reverse()
    i = lst.index(value)
    lst.reverse()
    return len(lst) - i - 1
    
    
def prefix_sum(arr, length_arr, prefix_sum):
    prefix_sum[0] = arr[0] 

    for i in range(1, length_arr): # 1, 2, 3, 4
        prefix_sum[i] =  prefix_sum[i-1]+ arr[i]
        
def suffix_sum(arr, length_arr, suffix_sum):
    suffix_sum[length_arr-1] = arr[length_arr-1] 

    for i in reversed(range(length_arr-1)): # 3, 2, 1, 0
        suffix_sum[i] = suffix_sum[i+1] + arr[i]

    
letters = [
    'a','b','c','d','e','f',
    'g','h','i','j','k','l',
    'm','n','o','p','q','r',
    's','t','u','v','w','x',
    'y','z']

 
# recursion limit fix decorator, change 'return' to 'yield' and add 'yield' before calling the function
def bootstrap(f):  
    stack = []
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

###############################################################################
###############################################################################
###############################################################################
mod = 10**9 + 7

def solve():
    n = int(input())
    arr = list(map(int,input().split()))
 


###############################################################################
###############################################################################
###############################################################################
 
for t in range(int(input())):
    # case(t+1)
    solve()
