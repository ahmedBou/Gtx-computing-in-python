hour = 1
minute = 1
time = "AM"
time2 = "PM"
if 10 <= hour < 11 and 0 <= minute <= 60:
    timex = str(str(hour) + ":" + str(minute)) + time2
    print("Go to Barrelhouse", timex)
else:3.2.
    if 11 <= hour < 2 and 0 <= minute <= 60:
        timex = str(str(hour) + ":" + str(minute)) + time
        print("Go to Taco Bell", timex)
    if 2 <= hour < 3 and 0 <= minute <= 60:
        timex = str(str(hour) + ":" + str(minute)) + time
        print("Go to Cookout", timex)
    else:
        print("Go to Waffle House")