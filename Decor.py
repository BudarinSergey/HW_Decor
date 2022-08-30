
import datetime

def cache(old_fun):

  def new_fun(*args, **kwargs):
    print(f'вызвана функция: {old_fun} с аргументами {args} и {kwargs}. Время вызова функции: {datetime.datetime.now()}')

    result = old_fun(*args, **kwargs)
    print(f'Результат {result}')
    return result
  return new_fun

@cache
def summ(a,b):
  return a+b


summ(2,6)
