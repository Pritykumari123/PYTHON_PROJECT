# date utilities
# Build a package to handle date operation with function like get_current_date and formatted_date.
import datetime
def get_current_date():
    return datetime.datetime.today()
def format_date(date):
    return date.strftime("%d-%b-%Y")   # %d= day of the month , %b= Month of short name , %Y= Year in full with century

current_date = get_current_date()
formatted_date = format_date(current_date)
print("current date:",current_date)
print("formatted date:",formatted_date)