
# if ((1 <= day <= 5 and "17:00" <= time <= "20:00") or 6 <= day <= 7 and "18:00" <= time <= "22:00") ) and from_station != "ZONE1" and to_station == "ZONE1":
#     is_peak_hour = False


from datetime import datetime
import constants


def calculate_fare(trips):
    for trip in trips:
        print(trip['datetime'].time())


def find_day(date):
    pass















journey_list = [
    {'datetime': datetime(2021, 2, 1, 10, 20, 0, 0), 'from': 2, 'to': 1},
    {'datetime': datetime(2021, 2, 1, 10, 45, 0, 0), 'from': 1, 'to': 1},
    {'datetime': datetime(2021, 2, 1, 16, 15, 0, 0), 'from': 1, 'to': 1},
    {'datetime': datetime(2021, 2, 1, 18, 15, 0, 0), 'from': 1, 'to': 1},
    {'datetime': datetime(2021, 2, 1, 19, 0, 0, 0), 'from': 1, 'to': 2}
]

calculate_fare(journey_list)