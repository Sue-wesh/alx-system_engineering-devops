#!/usr/bin/python3
"""
query redditApi
"""
import json
import requests
import sys


def top_ten(subreddit):
    """
    print the titles of the first 10 hot posts listed for a subreddit
    """
    subreddit = sys.argv[1]
    url = "http://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    agent_string = "API-query-reddit"

    titles = requests.get(url, headers={'User-Agent': agent_string})

    if titles.status_code != 200:
        print(None)
    else:
        json_response = titles.json()
        ten_titles = json_response.get('data').get('children')
        for new in ten_titles:
            title = new.get('data').get('title')
            print(ten_titles)
