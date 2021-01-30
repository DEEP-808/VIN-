n=int(input('Enter the number of students in calss  '))
a=0
b=0
c=0
res=[None]*3
for i in range(n):
  print(i+1,end="")
  name=input(' .Name ')
  print('enter subjects failed ')
  d=input().split()
  s=list(set(d))
  if len(d)!=len(s):
    print('Invalid input enter again')
    d=input().split()
  for ele in d:
      if(ele=='a'):
        a=a+1
      if(ele=='b'):
        b=b+1
      if(ele=='c'):
          c=c+1
  res.append(name)
  res.append('Subjects failed')
  res.append(d)
print(a,b,c,sep=" ")
if(a>b and a>c):
  print("The toughest subject is",'A')
if(b>a and b>c):
  print("The toughest subject is",'B')
if(c>a and c>b):
  print("The toughest subject is",'C')
