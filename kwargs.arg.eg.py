def shipping_label(*args, **kwargs):
   for arg in args:
      print(arg, end=" ")
   print()
   if "apt" in kwargs:
     print(f"{kwargs.get("street")} {kwargs.get("apt")} {kwargs.get("pobox")}")
   elif "pobox" in kwargs:
      print(f"{kwargs.get("street")}")
      print(f"{kwargs.get("pobox")}")
   else:
      print(f"{kwargs.get("street")}")
      
   print(f"{kwargs.get("city")} {kwargs.get("state")} {kwargs.get("zipcode")}")
         
shipping_label("Mr.", "Marvin", "Smith", "III",
                street = "123 main st",
                apt = "488",
                pobox = "Po box #1234",
                city = "Nairobi",
                state = "Nairobi",
                country = "Kenya",
                zipcode = "00100")