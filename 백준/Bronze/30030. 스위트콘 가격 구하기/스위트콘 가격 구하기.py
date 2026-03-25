import sys
import math
input = sys.stdin.readline

B = int(input().strip())

"""

A + A* 0.1 = B
A (1.1) = B
A = B / 1.1

"""

A = math.ceil(B / 1.1)

print(A)