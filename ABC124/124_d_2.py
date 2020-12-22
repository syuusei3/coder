N,k=map(int,input().split())
S=input()

nums=[]
now=1
seq_count=0
for char in S:
        if char == str(now):
            seq_count+=1
        else:
            now=1-now
            nums.append(seq_count)
            seq_count=1
nums.append(seq_count)
if len(nums)%2==0:
    nums.append(0)
sums=[0]*(len(nums)+1)

for i in range(len(nums)):
    sums[i+1]=sums[i]+nums[i]

ans=0
for i in range(1,len(sums),2):
    left=i-1
    right = min(i+2*k,len(sums)-1)
    ans=max(ans,sums[right]-sums[left])
print(ans)
