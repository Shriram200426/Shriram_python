a=[1,2,3,4,5]
for i in a:
    print(i)
    
print("indexing value:",a[1])

print("repitition",a*2)

b=[6,7,8]

print("concat",a+b)

a.append(8)
print(a)

a.extend(b)
print(a)

a.insert(5,7)
print(a)

a.insert(2,b)
print(a)

a.remove(7)
print(a)

a.pop()
print(a)

a.clear()
print(a)

del(a)