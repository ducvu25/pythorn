#chuỗi 
"""
VD: name1 = "vu duc"
    name2 = 'vu duc'
# Muốn sử dụng nháy đơn ta:
    void = "I'm duc"
# Muốn dùng nháy kép:
    void2 = 'I"m duc'

a = "vu' " + 'trung duc"'
b = 'Vu trung" '"duc'"
print(b)

#Chuỗi nhiều dòng
string = '''Vu
Trung
Duc'''
tương đương: string = 'Vu\nTrung\nDuc'

#Một số kí tự đặc biệt
\t: tab
\a: bíp
\b: backspace
\': dấu '
\": dấu "

#Chuỗi trần: Không chứa biết kí tự đặc biệt:
print(r'hello \neu gap nhau')

#Toán tử chuỗi
strA = 'Hello'
strB = "Cau"
strC = strA + " " + strB

#Toán tử nhân: nối n lần
strA = "hello"*5

#in: kiểm tra chuỗi có nằm trong chuỗi s
s = "Hello chao cau"
x = "cau"
kq= x in s

#lấy kí tự cuối
strB = "hello"
print(strB[-1])
#hoac: strB[len(strB) - 1]

#Cắt chuỗi
a = s[x:n:d] #Cắt từ vị trí x đi n kí tự với bước nhảy là d
kí hiệu None
VD
a = s[None:5:1]
b = s[0:None:1]
print(a)
print(b)

#Thay đổi xâu:
Vd s = "Xin chao"
Ta muốn đổi kí tự c thành C ta làm:
a = s[None:4:1] + "C" + s[5:None:1]
#Ép kiểu
VD chuyển từ xâu sang số:
x = int("76") + 5
str = str(67) + "5"

#Thay thế chuỗi
VD:
a = "Hello %s" %("Huong")
=> a = "Hello %s va %s" %("Huong", "Lan")
Hoặc:
s = "Hello %s va %s
traLoi = s %("lan", "huong")

#Toán tử f''
x = "Hello"
loiChao = f"{x} Lan, {x} Huong nhe"
loiChao2 = "%s Lan, %s Huong" %(x, x)

#Toán tử .format
x = "xin chao {0}, {2} va {1}".format('lan', 'huy', 'ngoc')

#Căn lề: '{:*n}'.format(<biến>)
{:^n}: Tạo n ô rồi căn giữa
{:<n}: Tạo n ô rồi căn trái
{:>n}: Tạo n ô rồi căn phải

#Một số hàm liên quan đến xâu trong py:



"""
a = 3586
b = 952
print('Tổng của {0} + {1} là: {2}\nHiệu của {0} - {1} là: {3}\nTích của {0} * {0} là: {4}\nThương của {0} / {1} là: {5}\n{0} chia {1} dư là: {6}'.format(a, b, a + b, a - b, a * b, a / b, a % b))