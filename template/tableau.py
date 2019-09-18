#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys
from math import sqrt,ceil
from copy import deepcopy

# Lecture de Table
N = int(input())
table = list()
for i in range(N):
    table.append(list(input()))