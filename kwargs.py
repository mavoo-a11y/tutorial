# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)

# print_address(street= "123 main st" ,
#               city= "Nirobi", 
#               state= "Nairobi", 
#               country ="Kenya", 
#               zipcode= "00100")

# def print_address(**kwargs):
#     for key in kwargs.keys():
#         print(key)

# print_address(street= "123 main st" ,
#               city= "Nirobi", 
#               state= "Nairobi", 
#               country ="Kenya", 
#               zipcode= "00100")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street= "123 main st" ,
              city= "Nirobi", 
              state= "Nairobi", 
              country ="Kenya", 
              zipcode= "00100")