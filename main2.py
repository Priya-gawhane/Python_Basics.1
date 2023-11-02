#lists

colleges = ['IIT','NIT','COE']

print(colleges[0])
print(colleges[2])
colleges[2] = "blue"
print(colleges[2])
print(colleges[1:3])

list2 =['a','b','c','d','e','f']

list2.append('g')
print(list2)
list2.insert(3, 'i')
print(list2)
print(max(list2))
print(min(list2))

# tuples example
tup1 = (1, 2, 3)
list1 = list(tup1)#how to convert tuple into list
print(list1)
print(tup1[0])

#dictionaries
names = {'harry': 22,
         'balloon': 10,
         'black': 23}
print(names.keys())