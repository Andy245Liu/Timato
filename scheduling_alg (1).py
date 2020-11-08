
from operator import itemgetter
from datetime import datetime

import sqlite3
conn = sqlite3.connect('Data.db')
c = conn.cursor()
# c.execute("SELECT Name, Type, Weighting, MentalEffort, Deadline, Duration, ScreenBlock, StartTime from Data")
cursor = conn.execute("SELECT Name, Type, Weighting, MentalEffort, Deadline, Duration, ScreenBlock, StartTime from Data")
data = cursor.fetchall()

today = datetime.today()

parsed_data = []
for i in range(0, len(data), 1):
    parsed_data.append([0] * 8)

static_data = []
dynamic_data_weights = []

cur_date = datetime.today().day
# cur_date = 6
free_times_by_day = [0] * 7  # assumption that index 1 represents Nov 8th

for i in range(0, len(free_times_by_day), 1):
    free_times_by_day[i] = []

def find_free_time():
    for i in range(0, len(parsed_data), 1):
        if parsed_data[i][1] == "\nStatic\n" or parsed_data[i][1] == "Static":
            static_data.append(parsed_data[i])

    min = 60 * 8
    max = 60 * 24

    for i in range(0, len(free_times_by_day), 1):
        free_times_by_day[i].append(min)

    for task in static_data:
        start_time_in_minutes = task[7].hour * 60 + task[7].minute
        free_times_by_day[task[7].day - cur_date].append(start_time_in_minutes)

        end_time_in_minutes = start_time_in_minutes + task[5]
        free_times_by_day[task[7].day - cur_date].append(end_time_in_minutes)


    for i in range(0, len(free_times_by_day), 1):
        free_times_by_day[i].append(max)

    for i in range(0, len(free_times_by_day), 1):
        set(free_times_by_day[i])


def parse_data():

    for task in range(0, len(data), 1):

        for col in range(0, 8, 1):
            parsed_data[task][col] = data[task][col]

        temp_str = data[task][4]

        if task == 0:
            parsed_data[task][4] = datetime.strptime(temp_str[1:20], '%Y-%m-%d %H:%M:%S')
        else:
            parsed_data[task][4] = datetime.strptime(temp_str, '%Y-%m-%d %H:%M:%S')

        temp_str = data[task][7]

        if task == 0:
            parsed_data[task][7] = datetime.strptime(temp_str[1:20], '%Y-%m-%d %H:%M:%S')
        else:
            parsed_data[task][7] = datetime.strptime(temp_str, '%Y-%m-%d %H:%M:%S')

def weighting_algorithm(weighting, deadline):
    today = datetime.today()

    today = datetime(today.year, today.month, today.day)
    deadline = datetime(deadline.year, deadline.month, deadline.day) # assumption that deadline is a date object
    delta_t = deadline - today

    days_to_deadline = delta_t.days
    total_weight_days_in_between = [0] * days_to_deadline
    daily_deadline_weight = 10 / days_to_deadline

    weighting_factor = 0.6
    deadline_weighting_factor = 0.4

    for i in range(0, days_to_deadline, 1):
        total_weight_days_in_between[i] = weighting * weighting_factor + daily_deadline_weight * i * deadline_weighting_factor

    return total_weight_days_in_between

def schedule_dynamic():
    parsed_data()

    day = 0
    while day < 7: # each day of the week, limit of 7 days

        for i in range(0, len(free_times_by_day), 1):
            del free_times_by_day[i][:]

        find_free_time()

        index_dynamic = []
        dynamic_data = []

        for i in range(0, len(parsed_data), 1):

            if parsed_data[i][1] == "\nDynamic\n" or parsed_data[i][1] == "Dynamic":
                dynamic_data.append(parsed_data[i])
                index_dynamic.append(i)

        if len(dynamic_data) == 0:
            return

        for i in range(0, len(dynamic_data), 1):
            dynamic_data_weights.append(weighting_algorithm(dynamic_data[i][2], dynamic_data[i][4]))

        max_free_block = 0
        i_max_free_block = 0

        for i in range(1, len(free_times_by_day[day]), 2):
            prev_max_free_block = max_free_block
            max_free_block = max(max_free_block, free_times_by_day[day][i] - free_times_by_day[day][i-1])

            if max_free_block > prev_max_free_block:
                i_max_free_block = i - 1

        max_weighting = 0
        i_max_weighting = 0

        for i in range(0, len(dynamic_data), 1):
            if len(dynamic_data_weights[i]) > day:
                if dynamic_data[i][5] <= max_free_block:
                    prev_max_weighting = max_weighting
                    max_weighting = max(max_weighting, dynamic_data_weights[i][day])

                    if max_weighting > prev_max_weighting:
                        i_max_weighting = i

        count = 0
        for i in range(0, len(dynamic_data), 1):
            if dynamic_data[i][5] > max_free_block:
                count += 1

            if count == len(dynamic_data):
                day += 1


        str_time = "2020-11-" + str(day + cur_date) + " " + str(free_times_by_day[day][i_max_free_block] // 60) + ":" + str(free_times_by_day[day][i_max_free_block] % 60) + ":00"

        parsed_data[index_dynamic[i_max_weighting]][7] = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
        temp_str = str(parsed_data[index_dynamic[i_max_weighting]][1].replace("Dynamic", "Static"))

        parsed_data[index_dynamic[i_max_weighting]][1] = temp_str
        # temp_time_str = datetime.strftime(datetime.strptime(parsed_data[index_dynamic[i_max_weighting]][7]), '%Y-%m-%d %H:%M:%S'))
        temp_time_str = datetime.strftime(parsed_data[index_dynamic[i_max_weighting]][7], '%Y-%m-%d %H:%M:%S')
        c.execute("UPDATE Data SET StartTime = '"+temp_time_str+"' WHERE Name = '"+parsed_data[index_dynamic[i_max_weighting]][0]+"'")
        # c.execute("UPDATE Data SET StartTime = '2020-11-10 16:00:00' WHERE Name = 'CIV102 Lecture'")
        # c.execute("UPDATE Data SET Weighting = 2 WHERE Name = 'CIV102 Lecture'")
        conn.commit()
