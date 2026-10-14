n = int(input())
seq = [int(x) for x in input().split()]

count = 1
seq.sort()

for i in range(n-1):
    if not seq[i] == seq[i+1]:
        count += 1

print(count)