#import math
import fractions

A,B,C,D=map(int,input().split())

sum1=(A-1)//C
sum2=B//C
sum3=sum2-sum1
sum1=(A-1)//D
sum2=B//D
sum4=sum2-sum1
num=(C*D)//fractions.gcd(C,D)
sum1=(A-1)//num
sum2=B//num
sum5=sum2-sum1
sum=sum3+sum4-sum5
sum=B-A+1-sum


print(sum)
