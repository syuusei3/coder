s=input()
ptn1=s[::2].count('0')+s[1::2].count('1')
ptn2=s[::2].count('1')+s[1::2].count('0')
print(min(ptn1,ptn2))
#omosiroinaaaa
#bekkai
"""
s=input()
x=s[::].count("0")+s[1::2].count("1")
print(min(x,len(s)-x))
"""
