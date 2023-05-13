"""
khai bao
    listA = ["xe may", "oto"]
do dai:
    len(listA)
truy cap
    listA[1], listA[-1]
them phan tu vao list:
    listappend("may bay") # dau
    listinsert(vi tri, "xe hoi")
in ra tung phan tu trong list
    for i in listA:
        print(i)
sap xep theo gia tri tang dan
    listsort()
"""
listA = ["xe may", "oto"]
print(len(listA))
print(listA[0], listA[-1])

listappend("may bay") # dau
listinsert(2, "xe hoi")

print("\nchua sap xep:")
for i in listA:
    print(i)

print("\nDa sap xep:")
listsort()
for i in listA:
    print(i)