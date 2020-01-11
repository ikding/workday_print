"""A python script to print out date strings for copy/paste into my work log.

Example usage:

    $ python workday_print.py 2016-08-02
    Work Log WW31 (2016)

    Mon (8/1):


    Tue (8/2):


    Wed (8/3):


    Thu (8/4):


    Fri (8/5):
"""
import argparse
import datetime


def this_weekday(d, weekday):
    """Get the date of the the first day of next week.

    Args:
        d (datetime.datetime): input datetime
        weekday (int): the weekday in integer. By Python convention,
            Monday is 0 and Sunday is 6
    """
    assert weekday <= 7
    days_ahead = weekday - d.weekday()
    return d + datetime.timedelta(days_ahead)


def this_weekday_list(d, num_days=5):
    """Get the list of 5 dates on and after the input date.

    Args:
        d (datetime.datetime): input date
        num_days (int): number of subsequent days we want to include.
            Defaults to ``5``.

    Returns:
        list of dates in datetime.datetime format.
    """
    date_list = [d + datetime.timedelta(i) for i in range(num_days)]
    return date_list


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get intput date')
    parser.add_argument('date_string', type=str,
                        help='Date contained in the week (e.g. 2016-07-31)')
    parser.add_argument('--nday', type=int,
                        help='Number of days we want to generate',
                        default=5, required=False)
    args = parser.parse_args()

    try:
        d = datetime.datetime.strptime(args.date_string, '%Y-%m-%d')
    except ValueError:
        print("Cannot parse date_string {0}. "
              "Please use YYYY-MM-DD format, such as: 2016-07-31"
              .format(args.date_string))
        raise

    title = 'Work Log WW{wk} ({yr})'.format(wk=d.isocalendar()[1],
                                            yr=d.isocalendar()[0])
    print(title)
    print("")

    for date_obj in this_weekday_list(this_weekday(d, 0), args.nday):
        print(date_obj.strftime("%a (%-m/%-d):"))
        # print("Breakfast: ")
        # print("Lunch: ")
        # print("Dinner: ")
        # print("Itinerary: ")
        print("")
        print("")
