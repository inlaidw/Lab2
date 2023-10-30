def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(pow(height, 2))
    print(bmi)
    if bmi < 18.5:
        return -1
    elif 18.5 <= bmi <= 25:
        return 0
    else:
        return 1



calculate_bmi(weight=57, height=1.73)
