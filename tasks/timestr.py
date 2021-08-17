__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    seconds_in_minute = 60
    seconds_in_hour = 60 * seconds_in_minute
    seconds_in_day = 24 * seconds_in_hour

    tmp_str = ''
    tmp = seconds // seconds_in_day
    if tmp:
        tmp_str += f'{tmp:02}d'
        seconds %= seconds_in_day

    tmp = seconds // seconds_in_hour
    if tmp:
        tmp_str += f'{tmp:02}h'
        seconds %= seconds_in_hour
    elif tmp_str:
        tmp_str += '00h'

    tmp = seconds // seconds_in_minute
    if tmp:
        tmp_str += f'{tmp:02}m'
        seconds %= seconds_in_minute
    elif tmp_str:
        tmp_str += '00m'

    tmp_str += f'{seconds:02}s'

    return tmp_str
