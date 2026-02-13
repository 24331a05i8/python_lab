list1 = [10, 20, 30]

print("Length of list:", len(list1))

list1.append(40)
print("After append:", list1)

list1.insert(1, 15)
print("After insert:", list1)

list2 = [50, 60]
list1.extend(list2)
print("After extend:", list1)

list1.remove(20)
print("After remove:", list1)

list1.sort()
print("After sort:", list1)
