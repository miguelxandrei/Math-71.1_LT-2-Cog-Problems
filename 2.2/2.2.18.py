n, num = [x for x in input().split()]
entries = [[x for x in input().split()] for i in range(int(n))]

winner_count = 0

for n in entries:
    if n[-1] == num:
        winner = n[0]
        winner_count += 1

if winner_count == 0 or winner_count > 1:
    print("no winner")
else:
    print(winner)