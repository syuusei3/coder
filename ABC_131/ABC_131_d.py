import sys
N=int(input())
number = []
for i in range(N):
    S, P = input().split(" ")
    number.append([S,P])

number.sort(key=lambda x: x[0])
number.sort(key=lambda x: x[1], reverse=True)
#number.sort(key=lambda x: x[0])
print(number)
"""
sum=0
for i in range(N):
    #print(number[i][0])
    sum+=int(number[i][0])
    if(sum>int(number[i][1])):
        print("No")
        sys.exit()
print("Yes")
"""
