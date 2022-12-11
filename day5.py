numbers = []
numbers.append(19)
print(numbers)
numbers.insert(1, 8)
numbers.insert(5, 7)
numbers.insert(3, 0)
print(numbers)
numbers.append(10)
print(numbers)
if 10 in numbers:
    print(numbers.index(10))
else:
    print("not in list")
print(numbers.pop())
print(numbers)
numbers.remove(7)
print(numbers)
numbers.reverse()
print(numbers)

#My solution
list = [5, 4, 8, 5, 1, 6, 4, 7, 4, 2]
copy =  list.copy()
for i in copy:
    if copy.count(i) > 1:
        while copy.count(i) > 1:
            copy.remove(i)
print(list)
print(copy)

#Mosh solution
ml = [5, 4, 8, 5, 1, 6, 4, 7, 4, 2]
uniques = []
for item in ml:
    if item not in uniques:
        uniques.append(item)
print(uniques)