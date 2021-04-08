def menu():
    print("[1] Carbon Dioxide")
    print("[2] Air")
    print("[3] Helium")
    print("[4] Hydrogen")

menu()
option = int(input("Enter your option: "))
numberofseconds = float(input("Number of seconds traveled: "))

if 0 < numberofseconds <= 30:
    while option != 0:
        if option == 1:
            print("Option 1 has been called")
            Totalmeters = 258.0 * numberofseconds
            print("Total Meters: ", Totalmeters)

        elif option == 2:
            print("Option 2 has been called.")
            Totalmeters = 331.5 * numberofseconds
            print("Total Meters: ", Totalmeters)

        elif option == 3:
            print("Option 3 has been called.")
            Totalmeters = 972.0 * numberofseconds
            print("Total Meters; ", Totalmeters)

        elif option == 4:
            print("Option 4 has been called.")
            Totalmeters = 1270.0 * numberofseconds
            print("Total Meters; ", Totalmeters)
        else:
            print("Invalid option")
else:
    print("Invalid Seconds")

    print()
    menu()
    option = int(input("Enter your option:"))
    numberofseconds = float(input("Number of seconds traveled: "))

print("Your Response is invalid. Thanks for using this program.   Goodbye.")
