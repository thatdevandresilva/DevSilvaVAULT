# date filtering: user can especify the range of the report (weekly or monthly) or start and end date
# only expenses within those dates can be printed
# sumarize the expenses per category
# sumarize the overall expenses within the range
# make the option to save the report as an csv or view it directly on the terminal
# csv should include: date of expense, category and amount

import datetime
import csv
from expense_tracker import pet, categories

def get_date_range():
    print("Report ranges: ")
    print("[1] Weekly")
    print("[2] Monthly")
    print("[3] Custom Date Range")

    while True:
        try:
            report_range = int(input("Select the report range: "))
            if 1 <= report_range <= 3:
                break
            else:
                raise ValueError
        except ValueError:
            return "Invalid! Choose a valid option"
        
    # today = 
    
    if report_range == 1:
        today = datetime.date.today()
        seven_days = datetime.timedelta(days=7)
        start_date = today - seven_days
        end_date = today
    elif report_range == 2:
        today = datetime.date.today()
        thirty_days = datetime.timedelta(days=30)
        start_date = today - thirty_days
        end_date = today
    elif report_range == 3:
        today = datetime.date.today()
        while True:
            try:
                format = "%b %d, %Y"
                start_date = input("Enter the start date (mmddyyyy): ")
                start_as_date = datetime.datetime.strptime(start_date, format).date()
                end_date = input("Enter the end date (mmddyyyy): ")
                end_as_date = datetime.datetime.strptime(end_date, format).date()
                break
            except ValueError:
                return "Invalid! Select a valid date."


def filter_expenses():
    pass

def sumarize_expenses():
    pass

def sumarize_per_category():
    pass

def generate_report():
    pass

def save_csv():
    pass

def report_generator():
    pass

report_generator(pet)