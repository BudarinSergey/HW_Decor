import time
import requests
from pprint import pprint
from Decor_path import parametrized_decor
import requests

FILE_PATH = 'decoratorlogs.txt'

@parametrized_decor(FILE_PATH)
def get_questions (tags):
    today_date = int(time.time())
    delta = 172800
    last_date = today_date - delta
    questions_list = []

    url = f'https://api.stackexchange.com/2.3/questions?&fromdate={last_date}&todate={today_date}&order=desc&sort=activity&tagged={tags}&site=stackoverflow'
    print(url)
    response = requests.get(url)
    for i in response.json()['items']:
        for d in i:
            questions_list.append(i['link'])

        return f'Количество вопросов с тегом "Python" : {len(questions_list) } \n Адреса ссылок: {questions_list}'

if __name__ == '__main__':
    print(get_questions('Python'))


# print (get_questions('Python'))