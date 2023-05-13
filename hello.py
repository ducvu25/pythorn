import math

s = input("Nhập tên của bạn: ")
print("Chào " + s + ", mình đến với thế giới lập trình")

print("Bảng chữ cái tiếng anh:")
for i in range(65, 65 + 26):
    print(chr(i))


def Draw(h):
    for i in range(0, h):
        for j in range(0, h + i):
            if j < h - i - 1:
                print(" ", end="")
            else:
                print("*", end="")
        print("")

    for i in range(0, int(h/2)):
        for j in range(0, 2*h - 2):
            if j < 1:
                print(" ", end="")
            else:
                print("*", end="")
        print("")


print("Cây thông")
h = int(input("Nhập vào chiều cao của tán cây: "))
Draw(h)


def CheckPrime(n):
   # n = int(a)
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print("Kiểm tra số nguyên tố")
n = int(input("Nhập số cần kiểm tra: "))
if (CheckPrime(n)):
    print(str(n) + " là số nguyên tố")
else:
    print(str(n) + " không là số nguyên tố")


def UCLN(a, b):
    if b == 0:
        return a
    return UCLN(b, a % b)


print("Tìm UCLN và BCNN")
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ nhất: "))
c = UCLN(a, b)
print("UCLN(" + str(a) + ", " + str(b) + ") = " + str(c))
print("BCNN(" + str(a) + ", " + str(b) + ") = " + str(a*b/c))
