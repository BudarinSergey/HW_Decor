
from datetime import datetime
import requests


FILE_PATH = 'decoratorlogs.txt'


def parametrized_decor(path):
    def decor(func):
        def new_foo(*args, **kwargs):
            date_time = datetime.now()
            func_name = func.__name__
            result = func(*args, **kwargs)
            with open(path, 'w', encoding='utf-8') as file:
                file.write(f'Дата/время: {date_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы: {args, kwargs}\n'
                           f'Результат: {result}\n')
            return result
        return new_foo
    return decor


@parametrized_decor(FILE_PATH)
def get_status(*args, **kwargs):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    print(get_status('https://yandex.ru/'))

