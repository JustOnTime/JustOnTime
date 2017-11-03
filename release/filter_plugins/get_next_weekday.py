import datetime

def get_next_weekday(startdate, weekday):
    """
    @startdate: given date, in format '2013-05-25T08:00:00Z'
    @weekday: week day as a integer, between 0 (Monday) to 6 (Sunday)
    """
    d = datetime.datetime.strptime(startdate, "%Y-%m-%dT%H:%M:%SZ")
    t = datetime.timedelta((7 + weekday - d.weekday()) % 7 + 7)
    return (d + t).strftime('%Y-%m-%dT%H:%M:%SZ')

class FilterModule(object):

    def filters(self):
        return {
            'get_next_weekday': get_next_weekday
        }
