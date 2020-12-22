n = int(input()[:4])
a = n//100
b = n%100
if 0<a<=12 and 0<b<=12:
    print('AMBIGUOUS')
elif 1<=a<=12 and (b>=13 or b==0):
    print('MMYY')
elif 1<=b<=12 and (13<=a or a==0):
    print('YYMM')
else:
    print('NA')

"""






"""
