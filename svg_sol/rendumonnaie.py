import sys

M = int(input())
T = int(input())
typ = []
nb = []
for i in range(T):
    a = input().rstrip('\n').split(" ")
    typ.append(int(a[1]))
    nb.append(int(a[0]))


def rend(M, sub):
    if len(sub) == 1:
        if (M % typ[sub[0]] == 0) and (M // typ[sub[0]] <= nb[sub[0]]):
            return M // typ[sub[0]]
        else:
            return 200
    elif M == 0:
        return 0
    else:
        el = sub.pop()
        lis = list()
        for i in range(nb[el] + 1):
            if M - i * typ[el] >= 0:
                lis.append(rend(M - i * typ[el], sub.copy()) + i)

        return min(lis)


a = rend(M, [i for i in range(T)])
if a >= 150:
    print('IMPOSSIBLE')
else:
    print(a)