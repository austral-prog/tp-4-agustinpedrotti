def leap_year():
    print("TO DO")
    year = int(input("ingrese un año: "))
    if year % 4 == 0:
        if year % 400 == 0 and year % 100 == 0:
            print (f"El año {year} es bisiesto")
        elif year % 100 != 0: 
            print (f"El año {year} no es bisiesto")
        else:
            print (f"El año {year} no es bisiesto")
