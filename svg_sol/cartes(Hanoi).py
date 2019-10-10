import  sys
""" Solution pour le problème Crapette du concours ORange 2019"""


lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

P = int(lines[0])
N = int(lines[1])


def aux_rec(pile_ini, pile_end, No):
    if No == 1:
        a = piles[pile_ini].pop()
        piles[pile_end] += [a]
        return [pile_end], [a]
    else:

        for i in range(P + 1):
            if i == pile_ini or i == pile_end:
                continue
            else:
                if len(piles[i]) == 0:
                    pile_aux = i
                    break
                else:
                    a = piles[i][len(piles[i]) - 1]
                    b = piles[pile_ini][len(piles[pile_ini]) - 1]
                    if a <= b + 1:
                        pile_aux = i
                        break

        sys.stderr.write(' '.join([str(pile_aux), str(P)]))

        pile_p, pil_t = aux_rec(pile_ini, pile_aux, No - 1)

        a = piles[pile_ini].pop()
        piles[pile_end] += [a]

        pile_p += [pile_end]
        pil_t += [a]

        pile_pb, pil_tb = aux_rec(pile_aux, pile_end, No - 1)

        return pile_p + pile_pb, pil_t + pil_tb


pile_ini = list(map(int, lines[2].split(' ')))

piles = [[] for piles in range(P + 1)]
piles[0] = pile_ini.copy()

if N > (P + 1):
    print('Fail')
elif N == 1:
    print(str(pile_ini[0]) + ' 1')
else:
    l1, l2 = aux_rec(0, 1, N)
print(';'.join([str(l2[i]) + ' ' + str(l1[i]) for i in range(len(l1))]))
