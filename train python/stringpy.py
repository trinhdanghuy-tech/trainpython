#Slicing
x = "Hello World"
print(x[2:5]) #llo
print(x[2:])   #llo World
print(x[:5])   #Hello
print(x[-5:-2]) #orl
#modify
y = "oc cho"
print(y.upper()) #OC CHO
print(y.lower()) #oc cho
#strip xoa khoang trang o cuoi chuoi
a = "  Chao ban nha   "
print(a.strip()) #Chao ban nha
print(a.lstrip()) #Chao ban nha
print(a.rstrip()) #  Chao ban nha
#replace sua bat ki 1 ky tu nao do
print(x.replace("H", "J")) #Jello World
#split tach chuoi thanh cac phan tu
print(x.split()) #['Hello', 'World']
print(y.split()) #['oc', 'cho']
#String Concatenation
z = x + " " + y
print(z) #Hello World oc cho
#Format
age = 36
print("Toi hien tai ".format(age)) #Toi hien tai 36
x = f("Toi ten huy, hien tai toi {age}") 
print(x) #Toi ten huy, hien tai toi 36
#Co the them :.2f vao de them so 0 dang sau
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
#String Escape Characters
#| Escape   | Ý nghĩa                     |
#| -------- | --------------------------- |
#| `\'`     | Dấu nháy đơn                |
#| `\"`     | Dấu nháy kép                |
#| `\\`     | Dấu gạch chéo ngược (`\`)   |
#| `\n`     | Xuống dòng                  |
#| `\t`     | Tab ngang                   |
#| `\r`     | Trở về đầu dòng             |
#| `\b`     | Backspace                   |
#| `\f`     | Form feed                   |
#| `\uxxxx` | Ký tự Unicode               |
#| `\ooo`   | Ký tự theo mã bát phân      |
#| `\xhh`   | Ký tự theo mã thập lục phân |
#String Methods
#1. Nhóm thay đổi chữ hoa/thường
#| Phương thức     | Mô tả                          | Ví dụ                                     |
#| --------------- | ------------------------------ | ----------------------------------------- |
#| `.upper()`      | Chuyển tất cả thành chữ hoa    | `"hello".upper()` → `"HELLO"`             |
#| `.lower()`      | Chuyển tất cả thành chữ thường | `"HELLO".lower()` → `"hello"`             |
#| `.title()`      | Chữ cái đầu mỗi từ viết hoa    | `"hello world".title()` → `"Hello World"` |
#| `.capitalize()` | Chữ cái đầu chuỗi viết hoa     | `"hello".capitalize()` → `"Hello"`        |
#| `.swapcase()`   | Đảo ngược hoa ↔ thường         | `"Hello".swapcase()` → `"hELLO"`          |
#2. Nhóm xóa/ký tự trắng
#| Phương thức | Mô tả                                                  | Ví dụ                          |
#| ----------- | ------------------------------------------------------ | ------------------------------ |
#| `.strip()`  | Xóa khoảng trắng hoặc ký tự chỉ định ở **đầu và cuối** | `"  hi  ".strip()` → `"hi"`    |
#| `.lstrip()` | Xóa bên trái                                           | `"  hi  ".lstrip()` → `"hi  "` |
#| `.rstrip()` | Xóa bên phải                                           | `"  hi  ".rstrip()` → `"  hi"` |
#3. Nhóm tìm kiếm & kiểm tra
#| Phương thức     | Mô tả                                            | Ví dụ                                |
#| --------------- | ------------------------------------------------ | ------------------------------------ |
#| `.find()`       | Trả về vị trí đầu tiên tìm thấy, -1 nếu không có | `"hello".find("l")` → `2`            |
#| `.rfind()`      | Vị trí cuối cùng tìm thấy                        | `"hello".rfind("l")` → `3`           |
#| `.index()`      | Giống `.find()` nhưng báo lỗi nếu không tìm thấy | `"hello".index("l")` → `2`           |
#| `.count()`      | Đếm số lần xuất hiện                             | `"banana".count("a")` → `3`          |
#| `.startswith()` | Kiểm tra chuỗi bắt đầu bằng...                   | `"python".startswith("py")` → `True` |
#| `.endswith()`   | Kiểm tra chuỗi kết thúc bằng...                  | `"python".endswith("on")` → `True`   |
#4. Nhóm thay thế
#| Phương thức      | Mô tả             | Ví dụ                                              |
#| ---------------- | ----------------- | -------------------------------------------------- |
#| `.replace(a, b)` | Thay `a` bằng `b` | `"hi hi".replace("hi", "hello")` → `"hello hello"` |
#5. Nhóm tách & nối
#| Phương thức     | Mô tả                 | Ví dụ                                                 |
#| --------------- | --------------------- | ----------------------------------------------------- |
#| `.split()`      | Tách chuỗi thành list | `"a,b,c".split(",")` → `["a","b","c"]`                |
#| `.splitlines()` | Tách theo dòng        | `"a\nb".splitlines()` → `["a","b"]`                   |
#| `.join(list)`   | Nối list thành chuỗi  | `" ".join(["I","love","Python"])` → `"I love Python"` |
#6. Nhóm kiểm tra định dạng
#| Phương thức  | Mô tả                | Ví dụ                              |
#| ------------ | -------------------- | ---------------------------------- |
#| `.isalnum()` | Chỉ gồm chữ & số     | `"abc123".isalnum()` → `True`      |
#| `.isalpha()` | Chỉ gồm chữ cái      | `"abc".isalpha()` → `True`         |
#| `.isdigit()` | Chỉ gồm số           | `"123".isdigit()` → `True`         |
#| `.isspace()` | Chỉ gồm khoảng trắng | `"   ".isspace()` → `True`         |
#| `.islower()` | Toàn chữ thường      | `"abc".islower()` → `True`         |
#| `.isupper()` | Toàn chữ hoa         | `"ABC".isupper()` → `True`         |
#| `.istitle()` | Kiểu tiêu đề         | `"Hello World".istitle()` → `True` |

#Boolean
print(bool(1))#True
print(bool(0))#False
print(bool(""))#False
print(bool("Hello"))#True
print(bool([]))#False
print(bool([1, 2, 3]))#True