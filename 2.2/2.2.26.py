n = int(input())
dominoes = [[int(x) for x in input().split()] for i in range(n)]

answer = "YES"

if dominoes[1][0] not in dominoes[0] and dominoes[1][-1] not in dominoes[0]:
    # checks if domino 1 can connect to domino 0, since we start at domino idx = 2 by default
    answer = "NO"
    print(answer)

else:

    for i in range(1, n):   # returns starting idx and its open side based on domino 0 and 1
        start_idx = i+1
        if dominoes[i] == dominoes[i-1] or dominoes[i] == dominoes[i-1][::-1]:
            continue   # skips identical dominoes at the start, since they can be whatever needed
        elif dominoes[i][0] in dominoes[i-1]:
            open_side = dominoes[i][-1]
            break
        elif dominoes[i][-1] in dominoes[i-1]:
            open_side = dominoes[i][0]
            break

    for i in range(start_idx, n):
        l1, r1 = dominoes[i]

        if l1 == open_side:
            open_side = r1
        elif r1 == open_side:
            open_side = l1
        else:
            answer = "NO"
            break
    
    print(answer)