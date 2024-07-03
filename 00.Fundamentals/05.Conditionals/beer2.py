beer = input()

if ' ' in beer and ':' in beer:
    hour_minutes, slot = beer.split()
    hour, minutes = hour_minutes.split(":")
    # Check if the characters for mitutes and hours are actually digits and also if they fall into the correct range. Also verify whether the daytime slot is one of the two possible
    if hour.isdigit() and minutes.isdigit() and 0 < int(hour) <= 12 and 0 <= int(minutes) <= 59 and (slot == "PM" or slot == "AM"):
        hour, minutes = int(hour), int(minutes)
        # In the scenario when the slot is PM,  add 12 hours - this approach uses a time range of 24 hours to ease the conditionals, but you could equally choose a different approach.
        if slot == "PM":
            hour += 12
        # Define the slots which represent the intervals for "beer time". Note that if the time is 12:00 PM, the transformed time is 24:00 hence it should be excluded.
        if 12 <= hour < 24 or hour < 3:
            print("beer time")
        else:
            # This "else" handles the scenarios when the interval is outside the "beer time" interval.
            print("non-beer time")
    else:
        # This "else" handles the scenarios when either the characters are not digits or if the values for hour and minutes are not valid ones.
        print("invalid time")
 
else:
    # This scenario handles the scenarios when we cannot properly split the input line.
    print("invalid time")