N = int(input())
P = int(input())
lines = []
for i in range(P):
    lines.append(input())


if P < N:
    print(" ".join([str(P), '0']))

last= N,0
for eta in range(P-N):
    if lines[eta] == 'D':
        last = [last[0] +1 , last[1]]
    elif lines[eta] == 'G':
        last = [last[0] -1 , last[1]]
    elif lines[eta] == 'B':
        last = [last[0]  , last[1]+1]
    else:
        last = [last[0]  , last[1]-1]
print(" ".join(list(map(str, last))))