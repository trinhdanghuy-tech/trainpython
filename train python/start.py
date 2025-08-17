word = 'test'
print(type(word))
# Hiển thị kiểu dữ liệu của biến word
print(dir(word))
# Hiển thị các phương thức và thuộc tính của biến word
print(word.upper())
#In hoa toàn bộ chữ
print(word.capitalize())
#In hoa chữ cái đầu
print(word.endswith('st'))
# Kiểm tra xem chuỗi có kết thúc bằng 'st' hay không
print(word.endswith('a'))
#Hàm funtion
def mysum(a, b):
    return a + b
print('Tổng của 2 và 3 là :', mysum(2, 3))
x = -1.5
y = abs(x)
# Hàm abs() trả về giá trị tuyệt đối của x
print('Giá trị tuyệt đối của -1.5 là:', y)