# n = 2
# print(1)
# print(200000,n-1)
# arr = []
# mask = (1 << 17) - 1
# fill = int((1 << 15) * 1.3 + 1)

# arr = []
# arr += [mask + 2] * 2
# x = 6
# for i in range(1, fill):
#     arr += [x] + [x]
#     x = x * 5 + 1
#     x = x & mask

# arr += [1] * (n - len(arr))
# print(*arr)
# # for i in range(n):
# #   print(arr[i], 1 + i)

n = 200000
print(1)
print(200000)
arr = []
mask = (1 << 17) - 1
fill = int((1 << 15) * 1.3 + 1)

arr = []
arr += [mask + 2] * 2
x = 6
for i in range(1, fill):
    arr += [x] + [x]
    x = x * 5 + 1
    x = x & mask

arr += [1] * (n - len(arr))
print(*(arr))

# for i in range(n):
#   print(arr[i], 1 + i)