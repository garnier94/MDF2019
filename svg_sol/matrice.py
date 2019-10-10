"""MDF 2014"""

#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

p = int(lines[0])
mat = []
for i in range(p):
    mat.append(list(map(int,lines[i+1].split(" "))))
    sys.stderr.write(lines[i+1] + '\n')

n = p//4
submat =[]
for i in range(n, 3*n):
    submat.append( [mat[j][i] for j in range(n, 3*n)])



mnini= min([min(submat[i]) for i in range(2*n)])
maxi = max([max(submat[i]) for i in range(2*n)])
moy = sum([sum(submat[i]) for i in range(2*n)]) /( 4* n)


count = [0 for j in range(maxi+1)]
for i in range(2*n):
    for j in range(2*n):
        count[submat[i][j]] += 1
mode= count.index(max(count))

print("%s %s %.1f %s" % (mnini, maxi, moy, mode))