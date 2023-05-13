#list
#cú pháp <biến> = [a, b, ..., "", "", ...]

#Khởi tạo list <tên biến > = [n for n in range(1, 4)]
# a = [n for n in range(1, 10)]
# print(a)

#ngoài ra: a = [n*10 for n in range(1, 100)]
# a = [n for n in range(1, 100)]
# print(a[2])

# a = list("hello")

#Toán tử

# +
# a = [1, 10]
# a += list("hello")
# print(a)

# *
# a = [1, 10, 3]
# a *= 3
# print(a)

# in

a = [1, 10, 3]
b = 10 in a
print(b == False)

