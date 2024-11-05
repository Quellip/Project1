from typing import List

list_words = [1, 2, 3, 4, 5]


def word_long(list_one: List[int]) -> List[str]:
    a = ''
    for num in list_one:
        a += str(num)
    return a


print(word_long(list_words))
