def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(pow(height, 2))
    print(bmi)
    if bmi < 18.5:
        print("underweight")
    elif 18.5 <= bmi <= 25:
        print("Normal weight")
    else:
        print("Overweight")


calculate_bmi(weight=57, height=1.73)
