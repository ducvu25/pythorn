# numbers = []
# strings = []
# names = ["John", "Eric", "Jessica"]

# # write your code here
# numbers.append(1)
# numbers.append(2)
# numbers.append(3)
# strings.append("hello")
# strings.append("world")
# second_name = names[1]


# # this code should write out the filled arrays and the second name in the names list (Eric).
# print(numbers)
# print(strings)
# print("The second name on the names list is %s" % second_name)



#Bai 2:
# x = object()
# y = object()

# # TODO: change this code
# x_list = [x]*10
# y_list = [y]*10
# big_list = x_list + y_list

# print("x_list contains %d objects" % len(x_list))
# print("y_list contains %d objects" % len(y_list))
# print("big_list contains %d objects" % len(big_list))

# # testing code
# if x_list.count(x) == 10 and y_list.count(y) == 10:
#     print("Almost there...")
# if big_list.count(x) == 10 and big_list.count(y) == 10:
#     print("Great!")

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%0.2f"

print(format_string % data)