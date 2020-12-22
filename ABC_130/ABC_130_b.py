N,X=map(int,input().split())
#L=input().split()
#直接リストに
L = list(map(int, input().split()))

"""
D=[]
D.append(0)
for i in range(0,N):
    D.append(D[i]+int(L[i]))
    m=i+1
    if(D[i+1]>X):
        break
"""
#こんなに難しく考える必要ない
ans = 1
t = 0
for i in L:
  t += i
  if t <= X:
    ans += 1

print(ans)
