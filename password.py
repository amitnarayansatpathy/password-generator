import random

val = input("Enter length of password: ")
print(val)


#for k in range(0,int(val)):
   #8
   #a[k]=0

num=input("Enter no of numbers in password")
alp=input("Enter no of alphabets in password")
spe=input("Enter no of special characters in password")

a=[0]*int(num)

for k in range(0,int(num)):
    a[k]=int(random.uniform(0,1)*9)

    
a1=[0]*int(alp)

for k in range(0, int(alp) ):
    a1[k]=chr(int(random.uniform(1,1.2577)*97))

a2=[0]*int(spe)
for k in range(0, int(spe )):
    b=random.randint(0,1)
    if b==0:
      a2[k]=chr(int(random.uniform(1,1.1034)*58))
    else:
      a2[k]=chr(int(random.uniform(1,1.054)*91))

print(a)
print(a1)
print(a2)

for i in a1 :
    a.append(i)

for i in a2 :
    a.append(i)

random.shuffle(a)

for k in range(0, len(a)):
   print(a[k], end="")




    