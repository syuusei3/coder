N=int(intput())

dic={}

for i in N:
    dic.append(input().split())
    dic[i][1]=int(dic[i][1])
    dic[i].append(i)
    print(dic)

dic=sorted(dic, lambda x:(x[0],-x[1]))

for j in range(N):
    print(dic[j][2]+1)
