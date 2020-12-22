S=int(input())

a=S/100
b=S%100

if((a>12 or a==0) and 1<=b<=12):
        print("YYMM")

elif(1<=a<=12 and (b>12 or b==0)):
        print("MMYY")

elif(1<=a<=12 and 1<=b<=12):
        print("AMBIGUOUS")

else:
    print("NA")
