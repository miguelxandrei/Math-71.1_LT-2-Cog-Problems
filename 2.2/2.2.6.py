n = int(input())
cards = []
for i in range(n):
    card = [x for x in input().split()]
    listed_card = [card[0], card[-1]]
    cards.append(listed_card)

for i in range(n):
    if cards[i][-1] == "Clubs" or cards[i][-1] == "Spades":
        cards[i].append("Black")
    else:
        cards[i].append("Red")

one_adjacent_color_counter = 0

for i in range(n):
    diff_suit_l = 0 if i-1 >= 0 and cards[i][-1] == cards[i-1][-1] else 1
    diff_suit_r = 0 if i+1 < n and cards[i][-1] == cards[i+1][-1] else 1
    if diff_suit_l != diff_suit_r:
        one_adjacent_color_counter += 1

print(one_adjacent_color_counter)