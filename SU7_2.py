# Thusano Masalesa
# 45312222
# Lottery Number Generator

"""
PSEUDOCODE:

1. Generate or select 7 unique lottery numbers.
2. If generating randomly, add numbers until the list has 7 unique values.
3. If selecting manually, prompt the user for 7 unique numbers.
4. Sort and display the numbers.
"""
import random

# Function to generate and return a sorted list of 7 unique random numbers between 1 and 49
def generateRandom():
    random.seed(111)  # Set seed for reproducibility (same numbers every time for testing)
    lottery_numbers = random.sample(range(1, 50), 7)  # Picks 7 unique numbers
    return sorted(lottery_numbers)  # Sorts the numbers in ascending order before returning

# Function to allow the user to manually enter 7 unique numbers between 1 and 49
def selectNumbers():
    selected_numbers = []
    print("Enter seven unique numbers between 1 and 49:")
    
    for i in range(7):  # Loop to collect 7 numbers
        while True:
            try:
                num = int(input("Enter number {}: ".format(i + 1)))  # Convert input to integer
            except ValueError:
                print("Invalid input. Please enter an integer.")  # Handle non-integer input
                continue
            
            if num < 1 or num > 49:
                print("Number must be between 1 and 49. Try again.")
                continue
            if num in selected_numbers:
                print("Number already selected. Try again.")
                continue
            
            selected_numbers.append(num)  # Add valid, unique number
            break  # Exit the loop once a valid number is entered

    return sorted(selected_numbers)  # Return the sorted list

# Function to display the list of lottery numbers in one line, sorted
def displayLottery(lottery_numbers):
    print("Lottery numbers:", end=" ")  # Print without newline
    for num in lottery_numbers:
        print(num, end=" ")  # Print each number followed by a space
    print()  # Final newline for clean output

# Main function to run the program
def main():
    lottery_numbers = [0] * 7  # Initialize a list with 7 zeros (just for initial display)
    print("Initial list of lottery numbers:", lottery_numbers)
    
    # Display user options
    print("Options:")
    print("1. Generate lottery numbers randomly")
    print("2. Select lottery numbers manually")
    
    option = input("Select an option (1 or 2): ")  # Take user input for option
    
    if option == '1':
        lottery_numbers = generateRandom()  # Call random generator
    elif option == '2':
        lottery_numbers = selectNumbers()  # Call manual selection
    else:
        print("Invalid option. Exiting program.")
        return  # Exit the program if input is not 1 or 2
    
    displayLottery(lottery_numbers)  # Show the final list of numbers

# Entry point of the program
if __name__ == "__main__":
    main()
