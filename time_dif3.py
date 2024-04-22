from datetime import datetime

def date_difference_in_days(date1, date2):
    # Convert the date strings to datetime objects
    datetime1 = datetime.strptime(date1, '%d/%m/%Y')
    datetime2 = datetime.strptime(date2, '%d/%m/%Y')

    # Calculate the difference in days
    difference_in_days= (datetime2 - datetime1).days
    
    # If the difference is negative, print the absolute value
    if difference_in_days < 0:
        print("The absolute difference in days is:", abs(difference_in_days))
    else:
        print("The difference in days is:", difference_in_days)

# Example 
date1 = '12/03/2021'
date2 = '09/08/2020'
date_difference_in_days(date1, date2)