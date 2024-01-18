import datetime


"""
Function Name: one_week
Input Params: due_date (string)
Description: Function calculates the dates for appointments a pregnant patient needs within 37-40 weeks of pregnancy. The expected due date is inclusive in weeks 37-40. The intervals between each appointment is one week during this stage of pregnancy.
Return Value: none
"""


def one_week(due_date):
    dates_count = 3
    day_count = 7
    weeks_away = 40
    print(due_date.strftime("%m/%d/%Y"), "(", weeks_away, "weeks away )")

    while dates_count > 0:
        one_interval = datetime.timedelta(day_count)
        third_stage_appt = due_date - one_interval

        dates_count -= 1
        weeks_away = weeks_away - 1

        print(third_stage_appt.strftime("%m/%d/%Y"), "(", weeks_away, "weeks away )")
        day_count = day_count + 7

    print("\n")


"""
Function Name: two_weeks
Input Params: due_date (string)
Description: Function calculates the dates for appointments a pregnant patient needs within 30-36 weeks of pregnancy. The intervals between each appointment is two weeks during this stage of pregnancy.
Return Value: none
"""


def two_weeks(due_date):
    dates_count = 4
    day_count = 28
    weeks_away = 36

    while dates_count > 0:
        two_interval = datetime.timedelta(day_count)
        second_stage_appt = due_date - two_interval

        dates_count -= 1

        print(second_stage_appt.strftime("%m/%d/%Y"), "(", weeks_away, "weeks away )")
        weeks_away = weeks_away - 2
        day_count = day_count + 14

    print("\n")


"""
Function Name: four_weeks
Input Params: due_date (string)
Description: Function calculates the dates for appointments a pregnant patient needs within 0-28 weeks of pregnancy. The intervals between each appointment is four weeks during this stage of pregnancy.
Return Value: none
"""


def four_weeks(due_date):
    dates_count = 8
    day_count = 83
    weeks_away = 28

    while dates_count > 0:
        month_interval = datetime.timedelta(day_count)
        first_stage_appt = due_date - month_interval

        dates_count -= 1

        print(first_stage_appt.strftime("%m/%d/%Y"), "(", weeks_away, "weeks away )")
        weeks_away = weeks_away - 4
        day_count = day_count + 28

    print("\n")


def main():
    # Display Title and Instructions
    print("Appointment Calculator")
    print("Please enter the Expected Due Date")

    # Receive the input
    exp_due_date = input("Expected Due Date (mm/dd/yyyy): ")
    exp_due_date = datetime.datetime.strptime(exp_due_date, "%m/%d/%Y")

    # Calculate next appointment
    one_week(exp_due_date)
    two_weeks(exp_due_date)
    four_weeks(exp_due_date)


if __name__ == "__main__":
    main()