import math as m
# Hàm math.sqrt() trả về căn bậc hai của 16
print(m.sqrt(16))
# Hàm math.pi trả về giá trị của số pi
print(m.pi)
# có thể thay math bằng một tên khác, ví dụ như m
from math import sin, pi
print(sin(0.5))
print(pi)
# Các lệnh điều kiện
True and True
# Kết quả là True
False and True
# Kết quả là False
True or False
# Kết quả là True
not True
# Kết quả là False
x = 30 # assign 30 to x
x >= 30 # is x greater than or equal to 30?
True
x > 15 # is x greater than 15
True
x > 30
False
x == 30 # is x the same as 30?
True
not x == 42 # is x not the same as 42?
True
x != 42 # is x not the same as 42?
True
# Lệnh if
x = 25
if x > 20:
    print('x lớn hơn 20')
else:
    print('x nhỏ hơn hoặc bằng 20')

def slength(str):
    if len(str) == 0:
        return 'chuỗi rong'
    elif len(str) < 10:
        return 'chuỗi ngắn'
    elif len(str) < 20:
        return 'chuỗi trung bình'
    else:
        return 'chuỗi dài'
print(slength('hihi'))
a = []
#lệnh append cho phép thêm ptu vào mảng
a.append(1)
a.append(2)
a.append(3)
print(a)
print(a[0])
max(a) #Kết quả là 3
min(a) #Kết quả là 1
a = "hello world"
print(a[5][7]) #Lỗi 
print(a[5:7]) #Kết quả là 'wo' trả về phần tử i và j-1
print(a[5:]) #Kết quả là 'world'
print(a[5])
print(a[6])
print('o' in a) #Kết quả là True
print(a + a) #Kết quả là 'hello worldhello world'
print(a * 3) #Kết quả là 'hello worldhello worldhello world'
t = (1, 5, 15)
print(type(t)) #Kết quả là <class 'tuple'>
print(t) #Kết quả là (1, 5, 15)
b = "Chao ban"
print(b + a) #Kết quả là 'Chao banhello world'
#ép kiểu dữ liệu
c = 5
d = "10"
print(c + int(d)) #Kết quả là 15
#Vòng lặp
for i in range(5):
    print(i)
animals = ['dog', 'cat', 'bird']
for pet in animals:
    print("This is {}".format(pet))
list(range(6)) 
tuple(range(6))
list(range(1, 10, 2)) #Kết quả là [1, 3, 5, 7, 9]
list(range(10, 0, -1)) #Kết quả là [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
list(range(5, 10)) #Kết quả là [5, 6, 7, 8, 9]
for letter in 'hello':
    print(letter)
def range_double(n):
    return [i * 2 for i in range(n)]
        
range_double(5) #Kết quả là 0, 2, 4, 6, 8

list(range(0, 10, 2)) #Kết quả là [0, 2, 4, 6, 8]

#Vong lap while
i = 0
while i < 5:
    print(i)
    i += 1
