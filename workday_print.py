'''
A small python script to print out date strings for copy/paste into my work log.

Example usage:

$ python workday_print.py 08/02/16
Work Log WW31 (2016)
Mon (8/1):


Tue (8/2):


Wed (8/3):


Thu (8/4):


Fri (8/5):

'''

import datetime
# from datetime import datetime, date, timedelta
import calendar
import argparse

parser = argparse.ArgumentParser(description='Get intput date')
parser.add_argument('date_string', help='Date contained in the week (e.g. 07/31/16)', type=str)

args = parser.parse_args()

try:
    d = datetime.datetime.strptime(args.date_string, '%m/%d/%y')
except ValueError:
    print "Cannot parse date_string {0}. Please use MM/DD/YY format, such as: 07/31/16".format(args.date_string)
    raise

def this_weekday(d, weekday):

    assert weekday <= 7
    days_ahead = weekday - d.weekday()
    # if days_ahead <= 0: # Target day already happened this week
    #     days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def this_weekday_list(d):

    date_list = [d + datetime.timedelta(i) for i in range(5)]
    # for i in range(5):
    #     date_list.append(d + datetime.timedelta(i))

    return date_list

title = 'Work Log WW{wk} ({yr})'.format(wk=d.isocalendar()[1],
                                        yr=d.isocalendar()[0])
print title

for date_obj in this_weekday_list(this_weekday(d, 0)):
    print date_obj.strftime("%a (%-m/%-d):")
    print ""
    print ""
