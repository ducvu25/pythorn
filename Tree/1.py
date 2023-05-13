# i = int(input("Nhap so nguyen: "))
# if i % 2 == 0:
#     print("So vua nhap la so chan.")
# else:
#     print("So vua nhap la so le.")

# c = input("Nhap chu cai: ")
# if c == 'y':
#     print("Doi khi y la nguyen am, doi khi y la phu am.")
# elif c in "ueoai":
#     print("Ki tu vua nhap la nguyen am.")
# else:
#     print("Ki tu vua nhap la phu am.")

# s = input("Nhap thang: ")
# if s in ["mot", "ba", "nam", "bay", "tam", "muoi", "muoi hai"]:
#     print("thang " + s + " co 31 ngay.")
# elif s == "hai":
#     print("thang " + s + " co 28 ngay neu khong phai nam nhuan, 29 ngay neu la nam nhuan.")
# else:
#     print("thang " + s + " co 30 ngay.")

# import math
# def canh_huyen(a, b):
#     return math.sqrt(a*a + b*b)

# a = float(input("Nhap do dai canh thu nhat: "))
# b = float(input("Nhap do dai canh thu hai: "))
# c = round(canh_huyen(a, b), 2)
# print("Do dai canh huyen cua tam giac la: " + str(c))

# a = []
# while True:
#     x = int(input("Nhap so nguyen - 0 de ket thuc: "))
#     if x == 0:
#         break
#     a.append(x);
# a.sort(reverse=False, key=None)
# for i in a:
#     print(i)

def count_chars_occuring_once(s):
    check = set()
    for c in s:
        if c not in check:
            check.add(c)
    count = 0
    for c in check:
        if s.count(c) == 1:
            count += 1
    return count

s = input("Nhap chuoi: ")
print("So ki tu xuat hien duy nhat la: " + str(count_chars_occuring_once(s)))