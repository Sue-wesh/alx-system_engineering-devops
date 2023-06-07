#!/usr/bin/python3
"""
queru Reddit API
"""
import json
import requests
import sys


def recurse(subreddit, hot_list=[]):
    """
    return a list containing the titles of all hot articles for given subreddit
    """
    url = "http://api.reddit.com/r/{}/hot".format(subreddit)
    u_agent = "API-query-reddit"

    titles = requests.get(url, headers={'User-Agent': u_agent})

    if titles.status_code != 200:
        return None
    else:
        json_resp = titles.json()
        hot_list.append(json_resp.get('data').get('title'))
        return hot_list
