from math import pi

def sanitize_results(input_str):
    try:
        parsed_float = float(input_str)
        return parsed_float
    except ValueError:
        print("Unable to parse float from string")
        exit(1)

def radians_converter():
    radians = sanitize_results(input("Enter the degrees: "))

    degrees = radians*(180/pi)
    print(f"{radians} radians is equal to {degrees:.2f} degrees" )

def degrees_converter():
    degrees = sanitize_results(input("Enter the radians: "))

    radians = degrees*(pi/180)
    print(f"{degrees} degrees is equal to {radians:.2f} radians" )

run = True

while run:
    try:
        convert = input("Would you like to convert to degrees or radians?")

        if convert.lower() == "radians" or convert.lower() == "r":
            radians_converter()

        elif convert.lower() == "degrees" or convert.lower() == "d":
            degrees_converter()

        else:
            print("Please type degrees or radians")
        
        again=str(input("Do you want another angle measurement converted, type yes or no: "))
        if again.lower() != "yes":
            run = False

    except ValueError:
        print("Invalid input detected. Please try again.")
        continue