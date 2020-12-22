import  math
N,D=map(int,input().split())

nums=[input().split()for i in range(N)]
sum=0
for i in range(N):
    for j in range(D):
        nums[i][j]=int(nums[i][j])
#print(nums)

def is_integer_num(n):
    if isinstance(n,int):
        return True
    if isinstance(n,float):
        return n.is_integer()
    return False

cout=0

for i in range(N-1):
    for j in range(i+1,N):
           for k in range(D):
               #print(nums[i][k])
               #print(nums[j][k])
               sum+=(nums[i][k]-nums[j][k])*(nums[i][k]-nums[j][k])

           sum=math.sqrt(sum)
           #print("##########")
           #print(sum)
           #print(type(sum))

           if is_integer_num(sum)==True:
                cout+=1
                sum=0
           else:
                sum=0

print(cout)
