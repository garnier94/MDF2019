# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

a = lines[0].split(' ')
N = int(a[0])
Q = int(a[1])

price_list = ['Err']
count_list = [0]
for i in range(1, N + 1):
    a = lines[i].split(' ')
    price_list.append(int(a[1]))
    count_list.append(int(a[0]))

if sum(count_list) < Q:
    print('MANIPULATION')

T = [[0 for i in range(Q + 1)] for j in range(N)]
for i in range(1, N):
    for c in range(Q + 1):
        if T[i - 1][c] == 0:
            T[i][c] = price_list[i]
        else:
            T[i][c] = min(T[i - 1][c], T[i - 1][max(0, c - count_list[i])] + price_list[i])

print(T[N - 1][Q])
