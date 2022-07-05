import time
import re

import requests


# Токен авторизации:
def take_last_posts():
    token = 'fd49e079fd49e079fd49e079acfd35ef03ffd49fd49e0799f06a98614884327e306da15'
    version = 5.131
    domain = 'clubvgek'
    count = 21
    offset = 1
    all_posts = []

    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'domain': domain,
                                'count': count,
                                'offset': offset
                            }
                            )

    data = response.json()['response']['items']
    all_posts.extend(data)
    time.sleep(0.5)
    return all_posts


def file_writer(data):
    all_days = ''
    for post in data:
        if re.search(r'ИЗМЕНЕНИЯ В РАСПИСАНИИ', post['text']):
            all_days += '\n\n' + post['text'] + '\n\n\n-----------------------------------------------------------'
    return all_days


def raspisanie():
    all_posts = take_last_posts()
    file_writer(all_posts)
