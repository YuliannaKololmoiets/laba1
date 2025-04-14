n=int(input())

A = list(map(int, input().split())) 
if n<=1 or n>=100:
    print('please choose n betwen 1 and 100')
for i in range(0, n):
    if A[i] <= -100 or A[i]>=100:
        print('please choose elements in range betwen -100 and 100')

non_increasing_k = 1
for i in range(1, n):
    if A[i] <= A[i - 1]:
        non_increasing_k += 1
    else:
        break

non_decreasing_k = 1
for i in range(1, n):
    if A[i] >= A[i - 1]:
        non_decreasing_k += 1
    else:
        break

print(max(non_increasing_k, non_decreasing_k))
