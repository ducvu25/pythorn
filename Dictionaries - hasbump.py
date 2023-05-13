phone = {}
phone["duc"] = "0342041436"
phone["lan"] = "0121241244"
print(phone)

# hoac
Phone = {
    "duc" : "0342041436",
    "lan" : "-124124124" "hello"
}
print(Phone)

#xuat tu dien
Sinhvien = {
    "1" : "duc",
    "2" : "an",
    "3" : "ngoc"
}
for id, name in Sinhvien.items():
    print(f"ma sinh vien {id} la cua sinh vien {Sinhvien[id]}")
# hoac
for id in Sinhvien:
    print(f"ma sinh vien {id} la cua sinh vien {Sinhvien[id]}")

# Xoa: del
del Sinhvien["1"]
print(Sinhvien)
#hoac pop
Sinhvien.pop("2")
print(Sinhvien)

phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}  

for name in phonebook:
    if(name == "Jill"):
        del phonebook[name]

# testing code
if "Jake" in phonebook:  
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")  