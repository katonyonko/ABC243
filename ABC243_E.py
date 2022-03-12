import io
import sys

_INPUT = """\
6
3 3
1 2 2
2 3 3
1 3 6
5 4
1 3 3
2 3 9
3 5 3
4 5 3
5 10
1 2 71
1 3 9
1 4 82
1 5 64
2 3 22
2 4 99
2 5 1
3 4 24
3 5 18
4 5 10
3 3
1 2 1
2 3 2
1 3 3
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  INF=10**20
  N,M=map(int,input().split())
  cost=[[INF]*N for i in range(N)]
  for i in range(N):
    cost[i][i]=0
  G=[[] for _ in range(N)]
  E=[]
  for i in range(M):
    a,b,c=map(int,input().split())
    a-=1; b-=1
    cost[a][b]=c
    cost[b][a]=c
    G[a].append((c,b))
    G[b].append((c,a))
    E.append((c,a,b))
  ans=0
  # cost[i][j]: 頂点v_iから頂点v_jへ到達するための辺コストの和
  for k in range(N):
      for i in range(N):
          for j in range(N):
              if cost[i][k]!=INF and cost[k][j]!=INF:
                  cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
  for i in range(M):
    tmp=0
    for j in range(N):
      if j!=E[i][1] and j!=E[i][2] and cost[E[i][1]][E[i][2]]==cost[E[i][1]][j]+cost[j][E[i][2]]:
        tmp=1
    ans+=tmp
  print(ans)