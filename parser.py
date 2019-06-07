import requests
import json


def take_posts():
    token = 'c45ec44cc45ec44cc45ec44c44c4346c04cc45ec45ec44c98bf5ad3af23f2d0e0fdc2ea'
    version = 5.95
    domain = 'eternalclassic'
    count = 10
    offset = 0
    all_posts = []

    while offset < 10000:
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
        offset += 500
    return all_posts


def json_write(all_posts):
    array = []
    for post in all_posts:
        if post['likes']['count'] > 1000 and len(post['attachments']) == 1:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            data = {}
            data['likes'] = post['likes']['count']
            data['date'] = post['date']
            data['url'] = img_url
            print(data)
            array.append(data)
    with open('eternalclassic.json', 'w') as file:
        json.dump(array, file)


p = take_posts()
# json_write(p)
