from operator import itemgetter
n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort(key = itemgetter(1))
now = 0
ans = "Yes"
for i in ab:
    a,b = i[0],i[1]
    now += a
    if now > b:
        ans = "No"
        break
print(ans)
