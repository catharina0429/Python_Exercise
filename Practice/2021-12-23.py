def date_time(time: str) -> str:
    """Date and Time Converter"""
    # d, t = time.split(" ")
    # Month = {'01': 'January', '02': 'February', '03': 'March', '04': 'April',
    #          '05': 'May', '06': 'Jun', '07': 'July', '08': 'August',
    #          '09': 'Sepember', '10': 'October', '11': 'November', '12': 'Decdember'}
    # d = list(map(str, d.split(".")))
    # d[0] = str(int(d[0]))
    # d[1] = Month[d[1]]
    # t = list(map(int, t.split(":")))
    # t = list(map(str, t))
    # return " ".join(d) + ' year ' + t[0] + ' hours ' + t[1] + ' minutes '
    from datetime import datetime
    t = datetime.strptime(time, "%d.%m.%Y %H:%M")
    y, m, d, h, min = t.year, datetime.strftime(t, "%B"), t.day, t.hour, t.minute

    return f'{d} {m} {y} year {h} hours {min} minutes'

if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")