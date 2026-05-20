WEIGHT=float(input('ENTER WEIGHT IN KG'))
HEIGHT=float(input("ENTER HEIGHT IN METER"))
BMI=WEIGHT/(HEIGHT * HEIGHT)
if BMI <= 18.5:
    print(f"your BMI is {BMI:.1f} and you are underweight")
elif BMI >= 25:
    print(f"your BMI is {BMI:.1f} and you are overweight")
else:
    print(f"your BMI is {BMI:.1f} and you are normal")