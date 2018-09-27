
# coding: utf-8

# In[55]:


from pprint import pprint
import requests
from urllib.parse import urlencode

APP_ID = input('Оставлять мои персональные айдишники с токенами не выглядит хорошей идеей, поэтому введите, пожалуйста, ID своего приложения: ')
OAUTH_URL = 'https://oauth.vk.com/authorize'
oauth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token'
}
print(' ')
print('Необходимо получить токен по данной ссылке, либо ввести имеющийся')
print('?'.join((OAUTH_URL, urlencode(oauth_data))))
print(' ')
TOKEN = input('Введите токен: ')
print(' ')
id1 = input('Введите id 1 пользователя: ')
id2 = input('Введите id 2 пользователя: ')


class User:
    
    def __init__(self, id):
        self.id = id
        
    def __and__(self, other):
        params = {
            'source_uid': self.id,
            'target_uid': other.id,
            'access_token': TOKEN,
            'v': '5.74'
        }
        response = requests.get('https://api.vk.com/method/friends.getMutual', params)
        return response.json()
    
        
user1 = User(id1)
user2 = User(id2)
rez = user1 & user2

pprint(rez)

