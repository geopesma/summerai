x = input("hours or minutes?")
if x=="hours":
    hours = int(input("how many hours?"))
    minutes= hours*60
    print(minutes)
elif x=="minutes":
    minutes = int(input("how many minutes?"))
    hours=minutes/60
    print(hours)