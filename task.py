# Написать функцию, которая получает на вход список чисел и возвращает новый список,
# содержащий только числа, которые являются палиндромами.
from typing import List

nums = [121, 123, 131, 34543]

def palindrom(spisok: List[int]) -> List[int]:
    """ Функция, выявляющаяся числа-палиндромы """
    list_num = []
    for num in nums:
        if str(num) == str(num)[::-1]:
            list_num.append(num)
    return list_num

print(palindrom(nums))

# [121, 131, 34543]