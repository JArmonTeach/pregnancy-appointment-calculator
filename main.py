import datetime


def one_week(due_date):
    week_interval_count = 3
    day_count = 7
    weeks_away = 40
    print(due_date.strftime("%m/%d/%Y"), "(", weeks_away, "weeks away )")

    while (week_interval_count > 0):
        one_interval = datetime.timedelta(day_count)
        third_stage_appt = due_date - one_interval
        week_interval_count -= 1
        weeks_away = weeks_away - 1
        print(third_stage_appt.strftime("%m/%d/%Y"), "(", weeks_away, "weeks away )")
        day_count = day_count + 7


def main():

    #Display Title and Instructions
    print("Appointment Calculator")
    print("Please enter the Expected Due Date")

    #Recieve the input
    first_appt = input("First Appointment Day (mm/dd/yyyy): ")
    first_appt = datetime.datetime.strptime(first_appt, "%m/%d/%Y")

    #Calculate next appointment
    one_week(first_appt)

if __name__ == "__main__":
    main()