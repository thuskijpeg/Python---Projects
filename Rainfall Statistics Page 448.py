# Rainfall Statistics


def main():
    highest = 0
    lowest = 100000
    average = 0
    total = 0
    highest_month = ""
    lowest_month = ""
    
    months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
    ]
    
    rainfall = []

    try:
        for month in months:
            rain = float(input(f"Enter total rainfall for {month}: "))
            rainfall.append(rain)

            if rain > highest:
                highest = rain
                highest_month = month

            if rain < lowest:
                lowest = rain
                lowest_month = month

            total += rain
    except Exception as err:
        print("An error has occured")
        print(f"Error: {err}")
    else:
        average = total / len(months)

        print(f"The average rainfall is {average:.2f}")
        print(f"Lowest Rainfall is {lowest:.2f} on month {lowest_month}")
        print(f"Highest Rainfall is {highest:.2f} on month {highest_month}")

if __name__ == "__main__":
    main()

    

