import io
import sys

_INPUT = """\
6
4
16
1
123456789012
1000000000000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  T=int(input())
  tmp=[1]
  dtmp=[1]
  now=0
  for i in range(10**5):
    while now**2<=i+2:
      now+=1
    tmp.append(dtmp[now-2])
    dtmp.append(dtmp[-1]+tmp[-1])
  for _ in range(T):
    X=int(input())
    l,r=1,3*10**9+1
    while r-l>1:
      mid=(l+r)//2
      if mid**2<=X: l=mid
      else: r=mid
    ans=0
    now=0
    while (now+1)**2<=l:
      ans+=(min((now+2)**2-1,l)-(now+1)**2+1)*dtmp[now]
      now+=1
    print(ans)