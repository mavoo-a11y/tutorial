def get_phone(Country, Area, first,last):
    return f"{Country} {Area} {first} {last}"

phone_num = get_phone(Country= +254, Area=123, first=456, last=7890)

print(phone_num)