A = list(map(int, input().split()))

counts = [0] * 10 
Array = []

for d in A:
    if d == 0:
        break
    counts[d] += 1
    Array.append(d)

print(*counts[1:10])

print(len(Array))

print(*sorted(Array))
