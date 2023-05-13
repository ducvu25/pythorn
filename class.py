# class MyClass:
#     variable = "blah"

#     DEF function(self):
#         print("This is a message inside the class.")

# myobjectx = MyClass()
# myobjecty = MyClass()

# myobjecty.variable = "yackity"

# # Then print out both values
# print(myobjectx.variable)
# print(myobjecty.variable)

# __init___()
# class NumberHolder:

#    DEF __init__(self, number):
#        self.number = number

#    DEF returnNumber(self):
#        return self.number

# var = NumberHolder(7)
# print(var.returnNumber()) #Prints '7'


# DEFine the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    DEF description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()
car1.name = "Fer"
car2.name = "Jump"
car1.kind = "convertible"
car2.kind = "van"
car1.color = "red"
car2.color = "blue"
car1.value *= 600 
car2.value *= 100
# test code
print(car1.description())
print(car2.description())