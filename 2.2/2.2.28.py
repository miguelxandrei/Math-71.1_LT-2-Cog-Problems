n, r = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

total_area = 0

for i in range(r): 
    # [KEY INSIGHT] each column is a trapezoid on its side: left side = base 1, right side = base 2, height = 1 unit
    side_a = min([abs(i - item) for item in a])   # [RECALL] 𝐴(𝑥) = min(|𝑥 − 𝑎1|, |𝑥 − 𝑎2|, |𝑥 − 𝑎3|, ..., |𝑥 − 𝑎𝑛|)
    side_b = min([abs(i + 1 - item) for item in a])
    total_area += (side_a + side_b) / 2

print(int(total_area))