def get_average(a1, a2, a3):
    return (a1 + a2 + a3) / 3


number = int(input("How many Students? "))

for x in range(number):
    print("Student", x + 1)

    name = input("Student Name: ")
    a1 = int(input("Activity 1: "))
    a2 = int(input("Activity 2: "))
    a3 = int(input("Activity 3: "))

    average = get_average(a1, a2, a3)

    if average >= 90:
        status = "Excellent"
    elif average >= 80:
        status = "Very Good"
    elif average >= 75:
        status = "Passed"
    else:
        status = "Failed"

    print("Name:", name)
    print("Activity 1:", a1)
    print("Activity 2:", a2)
    print("Activity 3:", a3)
    print("Average:", average)
    print("Status:", status)

