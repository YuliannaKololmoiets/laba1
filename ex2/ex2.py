n=int(input())
A = list(map(int, input().split()))
x=A[0]
x_pos=0
m=0

for step in range(n):
        min_idx = step

        for i in range(step + 1, n):
         
            if A[i] < A[min_idx]:
                min_idx = i

        if min_idx != step:
           A[step], A[min_idx] = A[min_idx], A[step]
           if x_pos == step:
            x_pos = min_idx
            m += 1
           elif x_pos == min_idx:
            x_pos = step
            m += 1

print(m)
