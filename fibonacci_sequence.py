def sanitize_results(input_str):
    try:
        parsed_int = int(input_str)
        return parsed_int
    except ValueError:
        print("Unable to parse int from string")
        exit(1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

run = True

while run:
    which_number = sanitize_results(input("Enter an integer for the fibonacci sequence: "))

    fibonacci(which_number)
    print(fibonacci(which_number))
    again=str(input("Do you want another fibonacci sequence, type yes or no: "))
    if again.lower() == "no" or again.lower() == "n":
        run = False