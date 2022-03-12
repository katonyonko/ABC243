import io
import sys

_INPUT = """\
6
25 10 11 12
30 10 10 10
100000 1 1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  V,A,B,C=map(int,input().split())
  V-=V//(A+B+C)*(A+B+C)
  if V<A: print('F')
  elif V<A+B: print('M')
  else: print('T')