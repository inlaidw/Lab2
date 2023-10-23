def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    get_user_input()

def get_user_input():
    userinput = input().split(",")
    userinput = [float(item) for item in userinput]
    print(userinput)
    calc_average_temperature(userinput)
    calc_min_max_temperature(userinput)

def calc_average_temperature(data):
    total = sum(data)
    avg = total / len(data)
    print("The average is : "+str(avg))


def calc_min_max_temperature(x):
    dmax = max(x)
    dmin = min(x)
    print("Min is: " + str(dmin) + " Max is: " + str(dmax))

def sort_temperature():
    print("List of Floats sorted in ascending order")


def calc_median_temperature():
    print("Float")


display_main_menu()