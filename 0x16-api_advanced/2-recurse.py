#!/usr/bin/python3
# queries all post using function recursive
""" reddit API """


import requests
import time


def recurse(subreddit, hot_list=[], after=""):
    '''list of all hot posts'''

    url = "https://www.reddit.com/r/" + subreddit + '/hot.json'
    headers = {'User-Agent': 'Python:Python_bot:v1.0 (by /u/paurbano)'}
    client = requests.session()
    client.headers = headers
    parameters = {'limit': 100, 'after': after}
    r = client.get(url, params=parameters)
    # print (r.json())
    if r.status_code == 200:
        after = r.json().get('data').get('after')
        for hot in r.json().get('data').get('children'):
            hot_list.append(hot.get('data').get('title'))
        if after is not None:
            # Sleep for one second to avoid going over API limits
            # time.sleep(1)
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
