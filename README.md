# Bank widget

## Описание
IT-отдел крупного банка делает новую фичу для личного кабинета клиента. 
Это виджет, который показывает несколько последних успешных банковских операций клиента. 
Вам доверили реализовать этот проект, который на бэкенде будет готовить данные для отображения в новом виджете.

## Инструкции
Продолжаем работу над виджетом банковских операций клиента. 
Выкладываем свой проект на GitHub и ведем разработку по GitFlow. 
Учитываем рекомендации PEP 8, продолжаем использовать линтеры и делаем атомарные коммиты.

# Задачи:

1. Создайте новые ветки в вашем репозитории для работы по _GitFlow_.

2. Создайте новый репозиторий на _GitHub_, который будет использоваться 
для хранения и совместной работы над вашим проектом.

3. Залейте содержимое вашего локального репозитория в созданный репозиторий на _GitHub_, используя команды 
`git add`, `git commit` и `git push`.

4. В директории **src** вашего проекта создайте модуль **processing**, 
который будет содержать новые функции обработки данных.

5. В модуле **processing** напишите функцию `filter_by_state`, 
которая принимает список словарей и опционально значение для ключа 
`state` (по умолчанию 'EXECUTED'). 
Функция возвращает новый список словарей, содержащий только те словари, у которых ключ 
`state` соответствует указанному значению.

```Примеры работы функции
# Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

# Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

6. В том же модуле напишите функцию `sort_by_date`, 
которая принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию - убывание). 
Функция должна возвращать новый список, отсортированный по **дате** (`date`).

```Примеры работы функции
# Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
```Пример входных данных для проверки функции
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

7. Создайте **README-файл** для вашего проекта, в котором описаны цель проекта, 
инструкции по установке и использованию разработанных функций, примеры работы с ними.


## Тестирование:

### Модуль masks

Функция get_mask_card_number:
Тестирование правильности маскирования номера карты.
Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи
и нестандартные длины номеров.
Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.
Функция

get_mask_account:
Тестирование правильности маскирования номера счета.
Проверка работы функции с различными форматами и длинами номеров счетов.
Проверка, что функция корректно обрабатывает входные строки, где номер счета меньше ожидаемой длины.

### Модуль widget

Функция mask_account_card:
Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки
в зависимости от типа входных данных
(карта или счет).
Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.

Функция get_data:
Тестирование правильности преобразования даты.
Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.

### Модуль processing

Функция filter_by_state:
Тестирование фильтрации списка словарей по заданному статусу state.
Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
Параметризация тестов для различных возможных значений статуса state.

Функция sort_by_date:
Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
Проверка корректности сортировки при одинаковых датах.
Тесты на работу функции с некорректными или нестандартными форматами дат.

### Модуль generators

Функция filter_by_currency:
Тесты проверяют, что функция корректно фильтрует транзакции по заданной валюте.
Проверяет, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
Генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций.

Функция transaction_descriptions:
Функция возвращает корректные описания для каждой транзакции.
Тестирует работу функции с различным количеством входных транзакций, включая пустой список.

Тестирование генератора card_number_generator:
Тесты проверяют, что генератор выдает правильные номера карт в заданном диапазоне.
Генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию.

### Модуль decorators

Для тестирования вывода в консоль применяетя фикстура capsys, которая позволяет перехватывать вывод данных в консоль.
Тесты покрывают различные сценарии использования декоратора, включая успешное выполнение функций и обработку исключений.

### Модуль reading_files

Добавлены функция и тест функции чтения файлов csv и excel.

### Модуль processing обновлён

Реализована основная функция. И дополнительно реализованы функции фильтрации по 
заданному слову и реализована функция подсчета количества банковских операций.