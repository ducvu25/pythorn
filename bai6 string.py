"""
Khai bao
    s = "hello word"
truy cap
    s[1], s[-1]
do dai:
    len(s)
kiem tra su xuat hien: strstr
    s1 = "hello"
    print(s1 in s)
cat chuoi: s[dau : cuoi : khoang cach]

hàm:

    Xóa kí tự đầu và cuối:
        strip() #khong làm thay đổi chuỗi sau khi sử dụng
    s1.strip('h')
    tách các từ thành list
        split()
    thay thế:
        replace()
    kiểm tra xuất hiện:
        startswitch("")
        endswitch("")
    tìm vị trí
        index(), find
    in hoa
        upper
    in thường
        lower
    Tên
        title()
    đếm
        count()
    formating
    % - .format() - f
    %:
        s = "duc"
        s1 = "hello %s" %duc
        Pi = 3.142214124
        s3 = f"hello {s}, so pi = {Pi:.2f}"
    Đảo ngược:
        s1 = s[ : :-1]
"""
# s = "hello word, my name is duc"
# s1 = " hello "
# print(s1 in s)
# print(s1.strip())
# print(s1)
# ls = s.split()
# print(ls)
# ls = s.split(',')
# print(ls)
# s3 = s.replace("duc", "phuong anh")
# print(s3)
# print(s.startswith("duc"))
# print(s.endswith("duc"))
# print(s.index("duc"))
# print(s.count("a"))

# s4 = "hello %s" % ls[-1]
# print(s4)
# Pi = 3.1424141
# s5 = f"hello {ls[-1]}, so pi = {Pi : .2f}"
# print(s5)
# astring = "Hello world!"
# afewwords = astring.split(" ")
# print(afewwords)

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))