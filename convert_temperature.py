def sanitize_results(input_str):
    try:
        parsed_float = float(input_str)
        return parsed_float
    except ValueError:
        print("Unable to parse float from string")
        exit(1)

def fahrenheit_converter(temp, target):
    celsius = (temp - 32) / 1.8
    kelvin = celsius + 273.15
    if target.lower() == "celsius" or target.lower() == "c":
        print(f"{temp:.2f} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius")
    elif target.lower() == "kelvin" or target.lower() == "k":
        print(f"{temp:.2f} degrees Fahrenheit is equal to {kelvin:.2f} Kelvin")
    else:
        print("Invalid target temperature measurement")
        return

def celsius_converter(temp, target):
    fahrenheit = (temp * 1.8) + 32
    kelvin = temp + 273.15
    if target.lower() == "fahrenheit" or target.lower() == "f":
        print(f"{temp:.2f} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit")
    elif target.lower() == "kelvin" or target.lower() == "k":
        print(f"{temp:.2f} degrees Celsius is equal to {kelvin:.2f} Kelvin")
    else:
        print("Invalid target temperature measurement")
        return

def kelvin_converter(temp, target):
    celsius = temp - 273.15
    fahrenheit = (celsius * 1.8) + 32
    if target.lower() == "celsius" or target.lower() == "c":
        print(f"{temp:.2f} Kelvin is equal to {celsius:.2f} degrees Celsius")
    elif target.lower() == "fahrenheit" or target.lower() == "f":
        print(f"{temp:.2f} Kelvin is equal to {fahrenheit:.2f} degrees Fahrenheit")
    else:
        print("Invalid target temperature measurement")
        return
run = True

while run:
    try:
        convert_from = input("Which temperature measurement do you want to convert from? (Fahrenheit/Celsius/Kelvin): ")
        convert_to = input("Which temperature measurement do you want to convert to? (Fahrenheit/Celsius/Kelvin): ")
        temperature = sanitize_results(input(f"Enter the temperature in {convert_from}: "))

        if convert_from.lower() == "fahrenheit" or convert_from.lower() == "f":
            fahrenheit_converter(temperature, convert_to)

        elif convert_from.lower() == "celsius" or convert_from.lower() == "c":
            celsius_converter(temperature, convert_to)

        elif convert_from.lower() == "kelvin" or convert_from.lower() == "k":
            kelvin_converter(temperature, convert_to)

        else:
            print("Invalid conversion requested")
            continue

        again=str(input("Do you want another temperature measurement converted, type yes or no: "))
        if again.lower() != "yes":
            run = False

    except ValueError:
        print("Invalid input detected. Please try again.")
        continue