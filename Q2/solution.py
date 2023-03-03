nooflines = input()
allValid = True
errorCodes = []
firstline = True
for i in range(0,int(nooflines)):
    s = input().split()
    if s[1] == "false":
      allValid = False
      errorCodes.append(s[2])

     
if allValid:
    print("Yes")
else:
    print("No")
    print(*errorCodes)
