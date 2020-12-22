import sys
S=input()
#print(type(S[0]))
#なんか詰まったよ


for i in range(3):
    if(S[i]==S[i+1]):
        print("Bad")
        sys.exit()
print("Good")
