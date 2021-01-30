#print('Enter the number of students in class') uncomment for console execution
def checkip(d):
    co=0
    for i in d:
        if( i=='a' or i=='b' or i=='c'):
            co+=1
    if(co==len(d)):
        return False
    else:
        return True
n=int(input())
a=0
b=0
c=0
res=[]
for i in range(0,n):
    #print(i+1,end="")  uncomment for console execution
    #print("Enter name of student ",end=" ") uncomment for console execution
    name=input()
    print(name)
    #print('enter subjects failed ') uncomment for console execution
    d=input().split()
    d.sort()
    print(len(d))
    if len(d)==0:
        continue
    s=sorted(list(set(d)))
    print(s)
    print(d)
    print(s!=d)
    if(s!=d or checkip(d)):
        print('Invalid input srart again ')
        exit()
    '''while len(d)!=len(s):
        print('Invalid input enter again')
        d=input().split()
        s=list(set(d)) ''' #uncomment for console execution
    for ele in d:
        if(ele=='a'):
            a=a+1
        if(ele=='b'):
            b=b+1
        if(ele=='c'):
            c=c+1
    l=[]
    #l.append(str(i+1))
    l.append(name)
    #l.append(' subjects failed ')
    l.append(' '.join(d))
    res.append(l)
    print(res)
#print(a,b,c,sep=" ")
print("Student data")
print('S.NO     name    subjects failed')
#print(len(res))
for i in range(len(res)):
    print(i+1,end=" ")
    print('  '.join(res[i]))
ans=max(a,max(b,c))
if(a==ans):
    print('Toughest subject is A')
if(b==ans):
     print('Toughest subject is B')
if(c==ans):
     print('Toughest subject is C')
