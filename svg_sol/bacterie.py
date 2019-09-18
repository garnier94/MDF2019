# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys
import copy

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

N = int(lines[0])

table = [[lines[j + 1][i] for i in range(N)] for j in range(N)]
str_int_list = [str(i) for i in range(N)]


def arrived(x, y, new):
    if y in str_int_list and x != y and new:
        return '='
    elif y == '#':
        return '#'
    elif y == '.':
        return x
    else:
        return y


N_max = 0
old_table = 0
while N_max < 200:
    new = [[0 for i in range(N)] for j in range(N)]
    old_table = copy.deepcopy(table)
    for i in range(N):
        for j in range(N):
            if old_table[i][j] in str_int_list + ['=']:
                if i + 1 < N:
                    table[i + 1][j] = arrived(old_table[i][j], table[i + 1][j], new[i + 1][j])
                    if table[i + 1][j] != old_table[i + 1][j]:
                        new[i + 1][j] = 1
                if i - 1 > -1:
                    table[i - 1][j] = arrived(old_table[i][j], table[i - 1][j], new[i - 1][j])
                    if table[i - 1][j] != old_table[i - 1][j]:
                        new[i - 1][j] = 1
                if j + 1 < N:
                    table[i][j + 1] = arrived(old_table[i][j], table[i][j + 1], new[i][j + 1])
                    if table[i][j + 1] != old_table[i][j + 1]:
                        new[i][j + 1] = 1
                if j - 1 > -1:
                    table[i][j - 1] = arrived(old_table[i][j], table[i][j - 1], new[i][j - 1])
                    if table[i][j - 1] != old_table[i][j - 1]:
                        new[i][j - 1] = 1
    N_max += 1

maxi = 0
for stri in str_int_list:
    nb = sum(sum(table[i][j] == stri for i in range(N)) for j in range(N))
    if nb > maxi:
        maxi = nb
print(maxi)
