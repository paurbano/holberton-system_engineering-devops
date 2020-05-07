#!/usr/bin/python3
# returns the number of subscribers for a given subreddit.
""" reddit API """


import requests


def number_of_subscribers(subreddit):
    '''number of subscribers'''
    url = "https://www.reddit.com/r/" + subreddit + '/about.json'
    headers = {'User-Agent': 'Python:Python_bot:v1.0 (by /u/paurbano)'}
    client = requests.session()
    client.headers = headers
    r = client.get(url)

    if r.status_code != 200:
        return 0
    else:
        return r.json().get('data').get('subscribers')
