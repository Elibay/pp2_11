# print("hello world")

# a = input("User input: ")

# a = 5
# b = 10

# s = "abc"
# print(s)

# s = input("User input: ")

# print(s + s)

# s = int(input())

# print(s + s)
# # +, -, *, /, %, ** -> pow

# print(s ** 3)

# str -> string a = "acsbbacb"
# int a = 3
# bool a = True, False
# float a = 3.14

# '' -> "" 

# a = [1, 2, 3, 4, 5]
# a[3] = 55
# print(a)

# a = (1, 2, 3, 4, 5)
# print(a)
# a[3] = 5
# print(a)
# a = "514x"
# # int() float()

# if a.isdigit():
#     print("Yes")
# else:
#     print("No")


# a = "abracadabra"
# print(a[3:])
# print(a[:3])
# print(a[3:5])
# print(a[-3:])
# print(a[:-3])

# a = "1,2,3,4,5"
# # print(a.title())
# # print(a.upper())
# print(a.split(','))
# print(a.replace(',', " "))

# name = 'John'
# age = 25
# formatted_string = f'My name is {name} and I am {age} years old.'
# print(formatted_string)

# # and # &&
# # or # ||
# # not # !
# a = False
# b = False
# if a and b: # () : == {}
#     print("All True")
# if a or b:
#     print("One of two")
# if not a and not b:
#     print("All False")

# x = int(input())
# if x % 4 == 0 and x % 100 != 0:
#     print("Yes")
# elif x % 4 == 0 and x % 400 == 0:
#     print("Yes")
# else:
#     print("No")

# # >, >=, <, <=, ==, != 

x = input()
if x.isdigit():
    x = int(x)
    print(x)
else:
    print("wrong format")