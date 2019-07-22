a=[]
num=int(input())
for i in range (5):
  a.append(int(input()))
flag=False
for j in range(5):
  for k in range(5):
    #a[j]+=a[k+1]
    if num == a[j]+a[k]:
      flag=True
      break
if flag:
  print("yes")
else:
  print("no")