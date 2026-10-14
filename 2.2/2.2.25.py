n, k, x = [int(x) for x in input().split()]
chests = [[int(x) for x in input().split()] for i in range(n)]

worst_case = 0
best_case = 0

for chest in chests:
    worst_case += min(chest)
    best_case += max(chest)

if x <= worst_case:
    print("ALWAYS")
elif worst_case < x <= best_case:
    print("SOMETIMES")
else:
    print("NEVER")