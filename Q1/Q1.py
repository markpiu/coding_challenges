
nl = []
ml = []
result = "Yes"
n = input()
nsizes = input()
m = input()
msizes = input()

if m > n:
  result = "No"
else:
  ns = nsizes.split()
  ms = msizes.split()
  for i in range(0,int(n)):
    if ns[i] == "M":
      nl.append(0)
    if ns[i][-1] == "S":
      nl.append(-len(ns[i]))
    if ns[i][-1] == "L":
      nl.append(len(ns[i]))


  for i in range(0,int(m)):
    if ms[i] == "M":
      ml.append(0)
    if ms[i][-1] == "S":
      ml.append(-len(ms[i]))
    if ns[i][-1] == "L":
      ml.append(len(ms[i]))

  nl.sort(reverse=True)
  ml.sort(reverse=True)
  for i in range(0,int(m)):
    if ml[i] > nl[i]:
      result = "No"
    


print(result)