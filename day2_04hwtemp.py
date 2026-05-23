#user enters a temperature and picks direction:
#C -- F, F-- C or C--K.
#Apply the correc formula. P rint result with 2 decimal place.

def C_F(celcius):
    fahrenheit_conv=(celcius * (9/5)) + 32
    print(f"The equivalent fahrenheit is {fahrenheit_conv:.2f}")
def F_C(fahrenheit):
    celcius_conv=(fahrenheit - 32) * (5/9)
    print(f"The equivalent celcius is {celcius_conv:.2f}")
def C_K(celcius):
    celciusk_conv=(celcius + 273.15)
    print(f"The equivalent kelvin is {celciusk_conv:.2f}")


convert_into=input("Enter 'A' for celcius into fahrenheit , 'B' for fahreheit into celcius, 'C' for celcius into kelvin :")
if convert_into.lower() ==  "a":
    celcius = float(input("Enter celcius:"))
    C_F(celcius)
elif convert_into.lower() ==  "b":
    fahrenheit=float(input("Enter fahreheit:"))
    F_C(fahrenheit)
elif convert_into.lower() ==  "c":
    celcius = float(input("Enter celcius:"))
    C_K(celcius)
else:
    print(f"Invalid choice")




