a=[1,2,3,4,5]
for i in a:
    print(i)
    
print("indexing value:",a[1])#indexing value

print("repitition",a*2)#repition

b=[6,7,8]

print("concat",a+b)#add two list

a.append(8)#add element at last 
print(a)

a.extend(b)#insert b list elements to a list elements 
print(a)

a.insert(5,7)#insert a element in specified index
print(a)

a.insert(2,b)#insert a list inside list
print(a)

a.remove(7)#remove a value 7
print(a)

a.pop(2)# removes a value based on index
print(a)

a.clear()#empty lit
print(a)

del(a)# delete completely

#slicing

a=[1,2,3,4,5,6,7,8,9,10,11,12]

print(a[1:])# start value is included

print(a[:5])# end value is not included

print(a[1:5])

b=['a','b','c','d',3,5,6,7]# for alphabets use ''

print(b[2])

#double slicing

print(a[1:13:2])# 3 value indicates step incremenet

print(a[0:11:2])

#reverse slicing

print(a[::-1])

print(a[::-2])# increment two value in reverse

# how to push required values in empty list
a=[1,2,3,4,5,6,7]
b=[]#empty list
for i in a:
    if i==1:
        print(i)
        b.append(i)#append used to push into empty list
print(b)        