import csv
import os


def main():
    # Define reasons dictionary
    reasons = {
        1: "Failed Last Hit",
        2: "Traded or Zoned",
        3: "Reset or Roamed",
        4: "Died",
        5: "Total CS",
    }
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    print("Enter the corresponding number each time you miss a CS:")
    print(
        "1 - Failed Last Hit\n2 - Traded or Zoned\n3 - Reset or Roamed\n4 - Died\ne - finish logging"
    )

    while True:
        user_input = input("Input: ")

        # Check if input is "e" for end of logging
        if user_input.lower() == "e":
            counts[5] = getFinalCS(False)
            break
        # Validate user input
        elif not user_input.isdigit() or int(user_input) not in [1, 2, 3, 4]:
            print("Invalid input. Please enter a number from 1-4, or 'e' to finish.")
        else:
            counts[int(user_input)] += 1

    # Check if file exists, if not, write headers
    if not os.path.isfile("Missed_CS_Data.csv"):
        with open("Missed_CS_Data.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(reasons.values())  # Write the headers

    # Append counts to csv
    with open("Missed_CS_Data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([counts[key] for key in sorted(counts.keys())])
        writer.writerow(
            [
                f"{round((100 * counts[key]) / (sum(counts.values())), 1)}%"
                for key in sorted(counts.keys())
            ]
        )


def getFinalCS(invalidInput):
    cs = input(
        "invalid Input, please enter and Integer:\nTotal CS:"
        if invalidInput
        else "Total CS:"
    )
    return int(cs) if cs.isdigit() else getFinalCS(True)


main()
