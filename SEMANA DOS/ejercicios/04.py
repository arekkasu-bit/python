year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:

       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))

#MEJORADO

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print(f"{year} es bisiesto")
else:
    print(f"{year} no es bisiesto")
