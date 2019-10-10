#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys


N = int(input())
lines = []
for i in range(N):
    lines.append(int(input()))


#Parcours doble
M = int(input())
N = int(input())
lines = []
r  =[]
for i in range(N):
    a =  input().split(" ")
    lines.append(int(a[0]))
    r.append(float(a[1]))

def ints():
    return list(map(int, input().split()))