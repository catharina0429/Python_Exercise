def date_time(time: str) -> str:
    """Date and Time Converter"""
    Month = {'01': 'January', '02': 'February', '03': 'March', '04': 'April',
             '05': 'May', '06': 'Jun', '07': 'July', '08': 'August',
             '09': 'Sepember', '10': 'October', '11': 'November', '12': 'Decdember'}

    hour = 'hour' if int(time[11:13]) == 1 else 'hours'
    minute = 'minute' if int(time[14:]) == 1 else 'minutes'
    return (str(int(time[:2])) + ' ' + Month[time[3:5]] + ' ' +
            time[6:10] + ' ' + 'year' + ' ' + str(int(time[11:13])) +
            ' ' + hour + ' ' + str(int(time[14:])) + ' ' + minute)

## Best Solution
    #     from datetime import datetime
    ## strptime : 문자열로부터 날짜와 시간 정보를 읽어서 datetime클래스 객체를 만듦
    ## strftime: 날짜와 시간정보를 문자열로 바꿔주는 함수
    #     dt = datetime.strptime(time, '%d.%m.%Y %H:%M')
    #     hour = 'hour' if dt.hour == 1 else 'hours'
    #     minute = 'minute' if dt.minute == 1 else 'minutes'
    #     return dt.strftime(f'%-d %B %Y year %-H {hour} %-M {minute}')

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