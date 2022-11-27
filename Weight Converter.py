

weight=float(input("Enter Your Weight: "))
unit=input("Kilograms or Pounds (K , L): ").lower()

if unit == "k":
  weight = weight * 2.205
  unit = "lbs."
  print(f"Your Weight is: {round(weight, 1)} {unit}")

elif unit == "l":
  weight = weight / 2.205
  unit = "kgs."
  print(f"Your Weight is: {round(weight, 1)} {unit}")

else:
  print(f"{unit} was not valid")
  