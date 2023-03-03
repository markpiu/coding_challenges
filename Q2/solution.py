

f = open("input.txt", "r")
Lines = f.readlines()
allValid = True
errorCodes = []
firstline = True
for record in Lines:
  if firstline:
    firstline = False
  else:
    s = record.split()
    if s[1] == "false":
      allValid = False
      errorCodes.append(s[2])

     
if allValid:
    print("Yes")
else:
    print("No",*errorCodes)