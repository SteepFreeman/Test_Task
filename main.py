"""
ДАНО:
dataset - датасет с фамилиями и показателями (тип показателя: integer).
footballers - список футболистов.
"""


dataset = {
    'admin$': 2,
    'daemon_': 6,
    'Kovalev': 16,
    'Anderson': 21,
    'Corvin': 3,
    'Borat': 23,
    'aBrams': 14,
    '13': 20,
    'Gerhaгd': 19,
    'Zidane': 12,
    'Messi': 10,
    'Rupert': 10
}


footballers = ['Messi', 'Zidane']


def parser_data(data, filter_name=None):
    if filter_name is None:
        filter_name = []
    cleared_dataset = {}
    for key, value in data.items():
        if str.isalpha(key) and key not in filter_name:
            if value % 2 != 0:
                value -= value % 2
            cleared_dataset.update({key: value})
        else:
            continue
    return cleared_dataset


def list_median(lst):
    lst.sort()
    middle = len(lst) // 2
    return (lst[middle] + lst[~middle]) / 2


def median_result(data):
    result = []
    keys = sorted(data, key=data.get, reverse=True)
    median = list_median(list(data.values()))
    for key in keys:
        if data[key] <= median:
            break
        result.append(key)
    return result


ds = parser_data(dataset, footballers)

print(median_result(ds))

"""
Thank too much for meet!
"""

"""
ЗАДАЧА:
ШАГ 1
Очистить датасет по совокупности условий:
1) Нам нужны только люди (фамилия состоит из букв)
2) Нам не нужны футболисты
3) Показатель может быть только чётным, остальное – искажения. Искажения исправить: привести к ближайшему меньшему чётному.
Вернуть очищенный словарь в переменной cleared_dataset.
ШАГ 2
Теперь небольшая аналитика на очищенном словаре. 
Надо вернуть список фамилий тех, у кого значение показателя выше медианного, в порядке убывания показателя.
Список поместить в переменной result.
"""
