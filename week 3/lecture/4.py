# int a_plus_b(int a, int b) {
#     return a + b
# }

def a_plus_b(a, b):
    return a + b


# print(a_plus_b(3, 5))

# def get_list_student(first="Azamat", second="Aisulu"):
#     print(first, second)

# def get_list_student(*, first, second):
#     print(first, second)

# get_list_student(first="Azamat", second="Aybol")

# def get_list_student(*args):
#     for i in args:
#         print(i)

def get_list_student(**kwargs):  # kew word arguments
    print(kwargs['first'])
    for key, value in kwargs.items():
        print(key, value)


get_list_student(first="Azamat", second="Aybol")
