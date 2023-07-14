import pandas as pd

csMissedPerLane = {
    "failedLastHit": 0,
    "zonedOrTraded": 0,
    "resetOrRoamed": 0,
    "died": 0
}

while True:
    user_input = input("Enter a number between 1-4, or 'quit' to exit: ")

    if user_input == "quit":
        total = sum(csMissedPerLane.values())
        csMissedPerLane["total"] = total
        percentages = {k: "{}%".format(v/total*100)
                       for k, v in csMissedPerLane.items()}
        df = pd.DataFrame([csMissedPerLane, percentages])
        df.to_excel("cs_missed_per_lane.xlsx", index=False)
        print("Counters saved to cs_missed_per_lane.xlsx")
        break
    elif user_input in ["1", "2", "3", "4"]:
        csMissedPerLane["failedLastHit"] += int(user_input == "1")
        csMissedPerLane["zonedOrTraded"] += int(user_input == "2")
        csMissedPerLane["resetOrRoamed"] += int(user_input == "3")
        csMissedPerLane["died"] += int(user_input == "4")
        print(csMissedPerLane)
    else:
        print("Invalid input, please enter a number between 1-4 or 'quit'")
