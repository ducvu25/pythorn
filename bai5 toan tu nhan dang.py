"""
Toán tử nhận dạng: is, is not
VD:
x = ["oto", "xe may"]
y = "may bay"
z = x
print("x is y: {0}".format(x is y))
print("x is z: {0}".format(x is z))
print("y is not z: {0}".format(y is not z))

Toan tu "in"
"""

# x = ["oto", "xe may"]
# y = "may bay"
# z = x
# print("x is y: {0}".format(x is y))
# print("x is z: {0}".format(x is z))
# print("y is not z: {0}".format(y is not z))
# print("x[1] in x: {0}".format(x[1] in x))
# print("x[0] in y: {0}".format(x[0] in y))
# print("x[1] in z: {0}".format(x[1] in z))

statement = False
another_statement = True
if statement is True:
    print(1)
    pass
elif another_statement is True: # else if
    print(2)
    pass
    print(4)
else:
    print(3)
    pass