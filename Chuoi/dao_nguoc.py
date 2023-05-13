
def Reversed(s):
    a = ""
    for i in s:
        a = i + a
    return a


s = input("Nhap chuoi can xu ly: ")
print("Chuoi vua nhap:\n" + s)
s = Reversed(s)
print("Chuoi sau khi dao nguoc:\n" + s)
