first_line = []
second_line = []
unique = True

first_line_input = input().split()
second_line_input = input().split()

def invalid_number(number):
    return number > 1000 or number < 1

try:
    # Convert inputs to integers
    first_line = [int(i) for i in first_line_input]
    second_line = [int(i) for i in second_line_input]

    # Validate: first line must contain exactly 2 numbers
    if len(first_line) != 2:
        exit()

    n, m = first_line

    # Validate number limits
    if invalid_number(n) or invalid_number(m):
        exit()

    # Validate length of second_line
    if m != len(second_line):
        exit()

    # Sort and check for uniqueness
    second_line.sort()
    for i in range(1, len(second_line)):
        if second_line[i] == second_line[i - 1]:
            exit()

    # Ensure the max number to check is not less than any number in the list
    if n < second_line[-1]:
        exit()

    # Output missing numbers in range 1 to n that are not in second_line
    for i in range(1, n + 1):
        if i not in second_line:
            print(i)

except:
    exit()
