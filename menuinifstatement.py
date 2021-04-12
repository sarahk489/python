Condition: bool = True


def menu():
    print("[1] Carbon Dioxide")
    print("[2] Air")
    print("[3] Helium")
    print("[4] Hydrogen")


while Condition:

    menu()

    option = int(input("Enter your option: "))
    numberofseconds = float(input("Number of seconds traveled: "))

    if 0 < numberofseconds <= 30 and option == 1:
        print("Option 1 has been called")
        Totalmeters = 258.0 * numberofseconds
        print("Total Meters: ", Totalmeters)

    elif 0 < numberofseconds <= 30 and option == 2:
        print("Option 2 has been called.")
        Totalmeters = 331.5 * numberofseconds
        print("Total Meters: ", Totalmeters)

    elif 0 < numberofseconds <= 30 and option == 3:
        print("Option 3 has been called.")
        Totalmeters = 972.0 * numberofseconds
        print("Total Meters; ", Totalmeters)

    elif 0 < numberofseconds <= 30 and option == 4:
        print("Option 4 has been called.")
        Totalmeters = 1270.0 * numberofseconds
        print("Total Meters; ", Totalmeters)

    else:
        print("Invalid Seconds or option, please try again.")

Condition: bool = False
