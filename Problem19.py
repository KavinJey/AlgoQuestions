#Date question

#1 Jan 1900 was a monday
#thirty days has september, april, june, and novemer, rest have 31, except feb who was 28 unless leap year

#how many sundays fell on the first of each month during the twenth century 1 jan 1901 to 31 dec 2000

start_day_of_week = 3


start_year = 1901
month_number = 0
sunday_count = 0


months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]

while start_year <= 2000:
    print(start_year, "this is the day:", start_day_of_week)

    if months[month_number] == "Jan":
        for x in range(1, 32):
            if start_day_of_week == 1:
                if x == 1:
                    sunday_count += 1

            start_day_of_week += 1

            if start_day_of_week > 7:
                start_day_of_week = 1


        month_number += 1

    if months[month_number] == "Feb":
        if start_year % 4 == 0:
            for x in range(1, 30):
                if start_day_of_week == 1:
                    if x == 1:
                        sunday_count += 1
                start_day_of_week += 1

                if start_day_of_week > 7:
                    start_day_of_week = 1
            month_number += 1

        else:
            for x in range(1, 29):
                if start_day_of_week == 1:
                    if x == 1:
                        sunday_count += 1
                start_day_of_week += 1
                if start_day_of_week > 7:
                    start_day_of_week = 1
            month_number += 1

    if months[month_number] == "March":
        for x in range(1, 32):
            if start_day_of_week == 1:
                if x == 1:
                    sunday_count += 1
            start_day_of_week += 1
            if start_day_of_week > 7:
                start_day_of_week = 1
        month_number += 1

    if months[month_number] == "April":
        for x in range(1, 31):
            if start_day_of_week == 1:
                if x == 1:
                    sunday_count += 1
            start_day_of_week += 1
            if start_day_of_week > 7:
                start_day_of_week = 1

        month_number += 1

    if months[month_number] == "May":
        for x in range(1, 32):
            if start_day_of_week == 1:
                if x == 1:
                    sunday_count += 1
            start_day_of_week += 1
            if start_day_of_week > 7:
                start_day_of_week = 1

        month_number += 1

    if months[month_number] == "June":
        for x in range(1, 31):
            if start_day_of_week == 1:
                if x == 1:
                    sunday_count += 1
            start_day_of_week += 1
            if start_day_of_week > 7:
                start_day_of_week = 1
        month_number += 1

    if months[month_number] == "July":
        for x in range(1, 32):
            if start_day_of_week == 1:
                if x == 1:
                    sunday_count += 1
            start_day_of_week += 1
            if start_day_of_week > 7:
                start_day_of_week = 1
        month_number += 1

    if months[month_number] == "Aug":
        for x in range(1, 32):
            if start_day_of_week == 1:
                if x == 1:
                    sunday_count += 1
            start_day_of_week += 1
            if start_day_of_week > 7:
                start_day_of_week = 1

        month_number += 1


    if months[month_number] == "Sep":
        for x in range(1, 31):
            if start_day_of_week == 1:
                if x == 1:
                    sunday_count += 1
            start_day_of_week += 1
            if start_day_of_week > 7:
                start_day_of_week = 1

        month_number += 1

    if months[month_number] == "Oct":
        for x in range(1, 32):
            if start_day_of_week == 1:
                if x == 1:
                    sunday_count += 1
            start_day_of_week += 1
            if start_day_of_week > 7:
                start_day_of_week = 1

        month_number += 1

    if months[month_number] == "Nov":
        for x in range(1, 31):
            if start_day_of_week == 1:
                if x == 1:
                    sunday_count += 1
            start_day_of_week += 1
            if start_day_of_week > 7:
                start_day_of_week = 1

        month_number += 1


    if months[month_number] == "Dec":
        for x in range(1, 32):
            if start_day_of_week == 1:
                if x == 1:
                    sunday_count += 1
            start_day_of_week += 1
            if start_day_of_week > 7:
                start_day_of_week = 1
        month_number = 0

    start_year += 1


print(sunday_count)