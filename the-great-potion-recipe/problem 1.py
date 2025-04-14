first_line = []
second_line = []
unique = True

first_line_input = input().split(" ")
second_line_input = input().split(" ")

def invalid_number(number):
    if number > 1000 or number < 1:
        return True
    else:
        return False
     
try:
    for i in first_line_input:
        first_line.append(int(i))

    for i in second_line_input:
        second_line.append(int(i))

    second_line.sort()

    for i in range(len(second_line)):
        if second_line[i] == second_line[i-1]:
            unique = False

    if invalid_number(first_line[0]) or invalid_number(first_line[1]):
        print("number must not be greater than 100 and less than 1")
    elif first_line[0] <= first_line[1] or first_line[0] > first_line[1]:
        print("enter valid inputs")
    elif first_line[0] < second_line[-1]:
        print("enter valid inputs")
    elif first_line[1] != len(second_line):
        print("enter valid inputs")
    elif len(first_line) != 2:
        print("enter valid inputs")
    elif unique:
        for i in range(first_line[0]):
            if i + 1 not in second_line:
                print(i+1)
    else:
        print("numbers must be unique")                      
except:
    print("enter valid inputs")
