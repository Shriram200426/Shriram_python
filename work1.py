
#sum of no
sum=0
i=1
while i<6:
    sum=sum+i
    i+=1
print(sum) 

#multiple of no
for i in range(1,11,1):
    print("11x",i,"=",11*i)

#factorial
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)

#check the first and lat letter of list are same
a=['abc','1231','aba','323','15a']
b=[]
for i in a:
  if i[0]==i[-1]:
    b.append(i)
print(b)
print(len(b))