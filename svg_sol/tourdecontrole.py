# *******
# * Read input from STDIN
# * Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
# * Use: sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys
import datetime

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

N = int(lines[0])
X = int(lines[1])
# sys.stderr.write(str(lines[N+1]))

list_hour = list()
list_piste = list()
a = 0

for i in range(2, N + 2):
    list_hour.append(datetime.datetime.strptime(lines[i][:5], '%H:%M'))
    list_piste.append(int(lines[i][6]))

for j, dt in enumerate(list_hour):
    if sum(list(map(lambda x: x < dt + datetime.timedelta(seconds=45 * 60), list_hour[j:]))) < X + 1:
        a = 1

for i, piste in enumerate(list_piste):
    for j in range(i, N):
        if list_piste[j] == piste:
            next_flight = j
            break
    if j == N:
        continue

    if (list_hour[next_flight] - list_hour[i]).seconds <= 360:
        a = 1

if not a:
    print('OK')
else:
    print('COLLISION')




