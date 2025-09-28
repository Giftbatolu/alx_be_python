#  datatime module
from datetime import datetime, timedelta, date

#  Display the current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # fortmat and print it
    print("Current data and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))

# Calculate a futute DAte
def calculate_future_date(days):
    # Get the current date
    # current_date = datetime.date.today()

    # Calculate future date
    future_date = date.today() + timedelta(days=days)
    #  Print the future date
    print("Future date: ", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":

    display_current_datetime()

    days_to_add = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days_to_add)