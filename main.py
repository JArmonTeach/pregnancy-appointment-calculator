import datetime

def main():

    #Display Title and Intructions
    print("Appointment Calculator")
    print("Please enter the date of the first appointment")

    #Recieve the input
    first_appt = input("First Appointment Day (mm/dd/yyyy): ")
    first_appt = datetime.datetime.strptime(first_appt, "%m/%d/%Y")

    #Calculate next appointment
    test_one = datetime.timedelta(days = 7)
    next_appt = first_appt + test_one
    print("Estimated next appointment will be on " + next_appt.strftime("%m/%d/%Y"))

if __name__ == "__main__":
    main()