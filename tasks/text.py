from typing import Optional
import re

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    shortest = None
    longest = None


    tmp = re.split('[\\s+,.]', text.strip())

    for i in tmp:
        if not i:
            continue

        if not shortest:
            shortest = i
        elif len(i) < len(shortest):
            shortest = i

        if not longest:
            longest = i
        elif len(i) > len(longest):
            longest = i

    return shortest, longest
