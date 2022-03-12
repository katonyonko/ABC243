import io
import sys

_INPUT = """\
6
4
1 3 5 2
2 3 1 4
3
1 2 3
4 5 6
7
4 8 1 7 9 5 6
3 5 1 7 8 2 6
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  ans=0
  for i in range(N):
    if A[i]==B[i]:
      ans+=1
  print(ans)
  print(len(set(A)&set(B))-ans)