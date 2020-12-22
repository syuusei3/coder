import itertools

N=int(input())
dic=[]


dic.append(input().split())
"""
for i in range(N-1):
    for t in range(i,N-1):
        p=dic[t+1][0]-dic[i][0]
"""
print(len(dic[0]))
#A=list(itertools.permutations(dic,N))
result=[]
for i in range(len(dic[0])):
    for j in range(len(dic[0])-1):
        for k in range(len(dic[0])-2):
            jData=listExcludedIndices(data,[0][i])
            kData=listExcludedIndices(jData,[0][j])

            result.append([data[i],jData[j],kData[k]])

print(result)
