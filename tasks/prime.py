__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if (number == 0) or (number == 1):  # частный случай
        return False

    k = 0
    for i in range(2, number // 2 + 1):
        if not (number % i):
            k += 1
    return not k
