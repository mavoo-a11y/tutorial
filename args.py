# def add(a, b):
#     return a + b

# print(add(1, 2))

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
    
# print(add(1, 2, 3, 4, 5))
    
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("John", "Smith")
