import io
import re
import sys

_INPUT = """\
6
2 1 2
2
1
3 3 2
1
1
1
3 3 10
499122176
499122175
1
10 8 15
1
1
1
1
1
1
1
1
1
1
"""
sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353
  N,M,K=map(int,input().split())
  W=[int(input()) for _ in range(N)]
  w=pow(sum(W),mod-2,mod)
  dp=[[[0]*(K+1) for j in range(M+1)] for i in range(N+1)]
  dp[0][0][0]=1
  F=[1]
  for i in range(K):
      F.append(F[-1]*(i+1)%mod)
  I=[pow(F[-1],mod-2,mod)]
  for i in range(K):
      I.append(I[-1]*(K-i)%mod)
  I=I[::-1]
  for i in range(N):
    for j in range(M+1):
      for k in range(K+1):
        for l in range(k+1):
          if l==0:
            dp[i+1][j][k]=(dp[i+1][j][k]+dp[i][j][k])%mod
          elif j>0:
            dp[i+1][j][k]=(dp[i+1][j][k]+F[k]*I[l]*I[k-l]*dp[i][j-1][k-l]*pow(w*W[i],l,mod))%mod
  print(dp[-1][-1][-1])