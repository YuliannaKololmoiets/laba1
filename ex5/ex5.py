n = int(input())
A = list(map(int, input().split()))
pos=[]
neg=[]
zero=[]
for i in range(n):
    if A[i]==0:
       zero.append(A[i])
    elif A[i]<0:
        neg.append(A[i])
    else:
        pos.append(A[i])
pos.sort()
neg.sort(reverse=True)
a=pos+neg+zero
print(*a)

    

