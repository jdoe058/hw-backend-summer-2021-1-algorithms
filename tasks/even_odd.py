__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    odd = 0
    even = 0
    for i in arr:
        if i & 1:
            odd += i
        else:
            even += i

    if odd:
        return even / odd
    else:
        return 0
