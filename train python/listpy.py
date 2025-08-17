thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist) # ['apple', 'banana', 'cherry', 'apple', 'cherry']
print(len(thislist)) # 5
#Co nhieu kieu list khac nhau
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#Ta co the truyen nhieu kieu du lieu khac nhau vao trong 1 list
list1 = ["abc", 34, True, 40, "male"]
print(type(list1)) # <class 'list'>
#Access Items
print(list1[0]) # abc
print(list1[1]) # 34
print(list1[2]) # True
print(list1[3]) # 40
print(list1[4]) # male
print(thislist[2:5]) # ['cherry', 'apple', 'cherry']
#Change List Items
thislist[1] = "blackcurrant"
print(thislist) # ['apple', 'blackcurrant', 'cherry', 'apple', 'cherry']
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # ['apple', 'blackcurrant', 'watermelon', 'apple', 'cherry']
#Lưu ý: Độ dài của danh sách sẽ thay đổi khi số mục được chèn không khớp với số mục được thay thế.
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# Ta co the chen 1 phan tu vao list
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry', 'apple', 'cherry']
#Append them phan tu vao cuoi list
thislist.append("orange")
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry', 'apple', 'cherry', 'orange']
#Extend ghep 2 list vao voi nhau
animals = ["cat", "dog", "rabbit"]
thislist.extend(animals)
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry', 'apple', 'cherry', 'orange', 'cat', 'dog', 'rabbit']
#Co the them bat ki iterable vao list
thistuple = ("kiwi", "mango")
thislist.extend(thistuple)
print(thislist) # ['apple', 'banana', 'watermelon', 'cherry', 'apple', 'cherry', 'orange', 'cat', 'dog', 'rabbit', 'kiwi', 'mango']
#Remove
thislist.remove("banana")
print(thislist) # ['apple', 'watermelon', 'cherry', 'apple', 'cherry', 'orange', 'cat', 'dog', 'rabbit', 'kiwi', 'mango']
#Pop xoa index theo mong muon
thislist.pop(1)
print(thislist) # ['apple', 'cherry', 'apple', 'cherry', 'orange', 'cat', 'dog', 'rabbit', 'kiwi', 'mango']
#Del dung de xoa phan tu
del thislist[0]
print(thislist) # ['cherry', 'apple', 'cherry', 'orange', 'cat', 'dog', 'rabbit', 'kiwi', 'mango']
#Clear xoa tat ca phan tu
thislist.clear()
print(thislist) # []
# Ta co the dung Loop trong list
#Vong lap for
list1 = ["apple", "banana", "cherry"]
for i in range(len(list1)):
    print(list1[i])  # apple banana cherry
#Vong lap While
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#List Comprehension cac cu phap ngan gon trong python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) # ['banana', 'mango']
#Sort sap xep lai list dc danh bang chu cai dau trong bang chu cai
thislist1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist1.sort()
print(thislist1) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
#1 vai vidu khac
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) #[23, 50, 65, 82, 100]
#Ta co the in ra dao nguoc bang cach su dung reverse
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
#Hoac co the su dung nhu sau
thislist.reverse()
print(thislist) # ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
# Sap xep voi key
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # ['banana', 'cherry', 'Kiwi', 'Orange']

#Copy
newlist = thislist.copy()
print(newlist) # ['banana', 'cherry', 'Kiwi', 'Orange']
#Hoac co the su dung list() method
newlist = list(thislist)
print(newlist) # ['banana', 'cherry', 'Kiwi', 'Orange']
#Hoac su dung slicing
newlist = thislist[:]
print(newlist) # ['banana', 'cherry', 'Kiwi', 'Orange']

#Join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
#cong 2 list voi nhau
list3 = list1 + list2
print(list3) # ['a', 'b', 'c', 1, 2, 3]
#dung vong lap for vaf append
for i in list2:
    list1.append(i)
print(list1) # ['a', 'b', 'c', 1, 2, 3]
#dung extend
list1.extend(list2)
print(list1) # ['a', 'b', 'c', 1, 2, 3, 1, 2, 3]