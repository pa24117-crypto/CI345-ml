# Homework 2 : Weekly Work Hours

NAMES = ["Tom", "Jane", "Mark"]
DAYS = ["MON", "TUE", "WED", "THU", "FRI"]

# create a two-dimensional array
hours = [[0]*5 for i in range(3)]


# method 1
def input_hours(hours, NAMES, DAYS):

    for i in range(len(NAMES)):
        print("Enter the work hours for", NAMES[i])

        for j in range(len(DAYS)):
            hours[i][j] = float(input(DAYS[j] + " : "))


# method 2
def display_hours(hours, NAMES, DAYS):

    print("\nDisplay Weekly Work Hours")
    print("\t", end="")

    for j in range(len(DAYS)):
        print(DAYS[j], end="\t")

    print()
    print("------------------------------------------")

    for i in range(len(NAMES)):
        print(NAMES[i], "|", end="\t")

        for j in range(len(DAYS)):
           print(hours[i][j], end="\t")
        print()


# method 3
def totalHours(hours, NAMES, DAYS):

    total = 0

    for i in range(len(NAMES)):

        for j in range(len(DAYS)):
            total += hours[i][j]
    return total


# method 4
def totalHoursByEmployee(hours, NAMES, DAYS):

    print("\nTotal Hours By Employee")
    print("----------------------------")

    for i in range(len(NAMES)):
        employeeTotal = 0

        for j in range(len(DAYS)):
            employeeTotal += hours[i][j]
        print(NAMES[i], "|", employeeTotal)


# invoke methods
input_hours(hours, NAMES, DAYS)
display_hours(hours, NAMES, DAYS)
print("--------------------------------")
print("Total hours :", totalHours(hours, NAMES, DAYS))
totalHoursByEmployee(hours, NAMES, DAYS)