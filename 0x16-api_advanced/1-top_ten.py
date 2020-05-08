#!/usr/bin/python3
# returns the number of subscribers for a given subreddit.
""" reddit API """


import requests


def top_ten(subreddit):
    '''number of subscribers'''
    url = "https://www.reddit.com/r/" + subreddit + '/hot.json'
    headers = {'User-Agent': 'Python:Python_bot:v1.0 (by /u/paurbano)'}
    client = requests.session()
    client.headers = headers
    parameters = {'limit': 10}
    r = client.get(url, params=parameters)
    # print (r.json())
    if r.status_code == 200:
        for hot in r.json().get('data').get('children'):
            print(hot.get('data').get('title'))
    else:
        print('None')
