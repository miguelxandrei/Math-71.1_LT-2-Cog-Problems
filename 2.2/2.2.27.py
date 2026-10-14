n = int(input())
x = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

possible = "YES"

x.sort()
c.sort()

for i in range(n):
    if c[i] < x[i]:
        possible = "NO"
        break

print(possible)