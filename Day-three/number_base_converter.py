def convert_number():
    print("🔢 Number Base Converter")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Decimal to Hex")

    choice = input("Choose option: ")

    try:
        if choice == "1":
            num = int(input("Enter decimal number (whole number only): "))
            print("Binary:", bin(num)[2:])

        elif choice == "2":
            num = input("Enter binary number: ")
            print("Decimal:", int(num, 2))

        elif choice == "3":
            num = int(input("Enter decimal number (whole number only): "))
            print("Hex:", hex(num)[2:])

        else:
            print("Invalid choice")

    except ValueError:
        print("❌ Invalid input! Please enter correct numbers only.")

convert_number()
