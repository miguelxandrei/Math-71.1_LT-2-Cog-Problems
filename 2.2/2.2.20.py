eq = list(input())
sum = int(eq[0])

for i in range(1, len(eq), 2):
    sum += int("".join(eq[i:i+2]))

print(sum)