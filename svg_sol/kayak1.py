# Lecture de Table
N = int(input())
table = list()
for i in range(N):
    table.append(list(input()))

    # PArcours en diagonale
nb_tab = [[0 for j in range(N)] for i in range(N)]
for iplusj in range(2 * N):
    for i in range(max(0, iplusj - N), min(N, iplusj)):
        j = iplusj - i - 1

        nb_tab[i][j] = int(table[i][j] == 'X')
        if i == 0:
            if j != 0:
                nb_tab[i][j] += nb_tab[i][j - 1]
        elif j == 0:
            nb_tab[i][j] += nb_tab[i - 1][j]
        else:
            nb_tab[i][j] += max(nb_tab[i - 1][j], nb_tab[i][j - 1])

print(nb_tab[N - 1][N - 1])