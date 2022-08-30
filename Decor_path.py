from datetime import datetime

FILE_PATH = 'decoratorlogs.txt'

def log_func (logs_file_path):
    with open(logs_file_path, 'w', encoding="utf-8") as file_obj:
        result1 = f'{datetime.now()}  n'
        file_obj.write(result1)


def cache(old_fun):

  def new_fun(*args, **kwargs):
    print(f'вызвана функция: {old_fun} с аргументами {args} и {kwargs}. Время вызова функции: {datetime.now()}')

    result = old_fun(*args, **kwargs)
    log_func(FILE_PATH)
    print(f'Результат {result}')
    return result


  return new_fun

# @cache
# def summ(a,b):
#   return a+b
#
#
# summ(2,6)