dic=[]

for i in range(5):
    dic.append(int(input()))

sub=[]
t=0

for line in dic:
    t+=line
    sub.append((10-line%10)%10)

t+=sum(sub)-max(sub)
print(t)
