n = int(input())
A = list(map(int, input().split()))

odd_indx = [A[i] for i in range(n) if i % 2 != 1]

odd_indx.sort(reverse=True)

j = 0
for i in range(n):
    if i % 2 != 1:
        A[i] = odd_indx[j]
        j += 1
print(*A)
