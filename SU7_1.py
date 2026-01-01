# Thusano Masalesa
# 45312222

# This program allows user to input 20 numbers
# Finding highest, lowest, total and average of numbers

# Finding the lowest number
def determineLowest(list):
    lowest = list[0]
    for number in list:
        if number < lowest:
            lowest = number
    return lowest


# Finding the highest number
def determineHighest(list):
    highest = list[0]
    for number in list:
        if number > highest:
            highest = number
    return highest


# Calculating the total of all numbers
def determineTotal(list):
    total = 0
    for number in list:
        total += number
    return total


# Calculating the average
def determineAverage(list, total):
    return total / len(list)


# Main program
def main():
    numbers = []
    count = 0
    

    for i in range(20):
        number = int(input("Enter a number: "))
        try:
            numbers.append(number)
            count += 1
        except ValueError:
            print("Invalid input. Please enter a number.")

    lowest = determineLowest(numbers)
    highest = determineHighest(numbers)
    total = determineTotal(numbers)
    average = determineAverage(numbers, total)

    # Displaying the results
    print("Lowest number:", lowest)
    print("Highest number:", highest)
    print("Total of numbers:", total)
    print("Average of numbers:", average)


if __name__ == "__main__":
    main()
