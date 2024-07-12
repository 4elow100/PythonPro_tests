import requests


# Код из тренажера "Квадратные уравнения"

def discriminant(a, b, c):
    return b * b - 4 * a * c


def quad_equation(a, b, c):
    if discriminant(a, b, c) < 0:
        return 'корней нет'
    elif discriminant(a, b, c) == 0:
        return f'{-b / (2 * a)}'
    else:
        return f'{(-b + discriminant(a, b, c) ** 0.5) / (2 * a)} {(-b - discriminant(a, b, c) ** 0.5) / (2 * a)}'


# Код из тренажера "Бравый сисадмин"

def brave_sysadmin(models: list, available: list, manufacturers: list):
    repair_count = 0
    ssds = []
    for i in range(len(models)):
        if available[i] == 1:
            for j in range(len(manufacturers)):
                if manufacturers[j] in models[i]:
                    ssds.append(models[i])
                    repair_count += 1
    return ssds, repair_count


# Код из тренажера "Знакомства"

def acquaintance(boys: list, girls: list):
    result = ""
    if len(boys) == len(girls):
        for b, g in zip(sorted(boys),
                        sorted(girls)):
            result += f'{b} и {g}, '
        result = result[:-2:]
    else:
        result = "Кто-то может остаться без пары!"
    return result


# Код функции для работы с Яндекс.Диск REST API

def api_yandex(token, path):
    headers = {'Authorization': f'OAuth {token}'}
    params = {'path': path}
    url = f'https://cloud-api.yandex.net/v1/disk/resources'
    response = requests.put(url, headers=headers, params=params)
    return response
