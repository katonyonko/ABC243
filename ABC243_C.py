import io
import sys

_INPUT = """\
6
3
2 3
1 1
4 1
RRL
2
1 1
2 1
RR
10
1 3
1 4
0 0
0 2
0 4
3 1
2 4
4 2
4 4
3 3
RLRRRLRLRR
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  p=[list(map(int,input().split())) for _ in range(N)]
  S=input()
  pp=[(p[i][1],p[i][0],0) if S[i]=='L' else (p[i][1],p[i][0],1) for i in range(N)]
  pp.sort(key=lambda x:x[0])
  ans='No'
  i=0
  while i<N:
    l,r=-(10**10),10**10
    if pp[i][2]==0: l=max(l,pp[i][1])
    else: r=min(r,pp[i][1])
    while i<N-1 and pp[i+1][0]==pp[i][0]:
      if pp[i+1][2]==0: l=max(l,pp[i+1][1])
      else: r=min(r,pp[i+1][1])
      i+=1
    if r<l: ans='Yes'
    i+=1
  print(ans)