n = int(input())
A = list(map(int, input().split()))
k = int(input())
s = 0
A_sort = sorted(A)
B = A.copy() 
for i in range(n - k):
    if B[i] > B[i + k]:
        B[i], B[i + k] = B[i + k], B[i]
        s += 1

if B != A_sort:
    s = -1

print(s)
