import random

while True:
    n = int(input('Nhap so nguyen luong phan tu: '))
    if n <= 0:
        print("Vui long nhap so luong lon hon 0!\n")
    else:
        break

a = []
for i in range(n):
    a.append(random.randint(-100, 100))

print("Day duoc tao:\n")
print(a)
a.sort()
print("Day so le:")
for i in a:
    if (i % 2 == 1):
        print(i, end=" ")

print("\nDay so chan:")
for i in a:
    if (i % 2 == 0):
        print(i, end=" ")
