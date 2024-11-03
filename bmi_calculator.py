
weight = int(input())
height = float(input())

ibm = weight/height**2

if ibm > 30:
    print("Obesity")
elif ibm >= 25 and ibm <= 30:
    print("Overweight")
elif ibm >= 18.5 and ibm < 25:
    print("Normal")
else:
    print("Underweight")