from datetime import time

zones  = [1,2]
default_peak_hours = [(time(7, 00), time(10, 30)), (time(17, 00), time(20, 00))]

peak_hours = {
    1: default_peak_hours,
    2: default_peak_hours,
    3: default_peak_hours,
    4: default_peak_hours,
    5: default_peak_hours,
    6: [(time(9, 00), time(11, 00)), (time(18, 00), time(22, 00))],
    7: [(time(9, 00), time(11, 00)), (time(18, 00), time(22, 00))]
}

peak_fare_chart = {
    1: {
        1: 30,
        2 : 35
    },
    2: {
        1: 35,
        2: 25
    }
}

off_peak_fare_chart = {
    1: {
        1: 25,
        2 : 30
    },
    2: {
        1: 30,
        2: 20
    }
}

daily_cap = {
    1: {
        1: 100,
        2: 120
    },
    2: {
        1: 120,
        2: 80
    }
}

monthly_cap = {
    1: {
        1: 500,
        2: 600
    },
    2: {
        1: 600,
        2: 400
    }
}