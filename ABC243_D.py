import io
import sys

_INPUT = """\
6
3 2
URL
4 500000000000000000
RRUU
30 123456789
LRULURLURLULULRURRLRULRRRUURRU
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,X=map(int,input().split())
  S=input()
  d=[]
  for i in range(N):
    if S[i]=='U':
      if len(d)>0 and d[-1]!='U': d.pop()
      else: d.append('U')
    else: d.append(S[i])
  for i in range(len(d)):
    if d[i]=='U': X//=2
    elif d[i]=='L': X*=2
    else: X=2*X+1
  print(X)