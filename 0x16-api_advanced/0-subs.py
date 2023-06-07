#!/usr/bin/python3
"""
return the total no of subscribers for a given subreddit
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """
    if in invalid subreddit is given return 0
    """
    url = "http://api.reddit.com/r/{}/about".format(subreddit)
    agent_string = "API-query-reddit"

    subs = requests.get(url, headers={'User-Agent': agent_string})

    if subs.status_code != 200:
        return 0
    else:
        json_response = subs.json()
        subs_num = json_response.get('data').get('subscribers')
        return subs_num
