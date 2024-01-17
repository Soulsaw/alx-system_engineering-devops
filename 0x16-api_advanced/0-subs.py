#!/usr/bin/python3
"""API Advanced"""
import requests


def number_of_subscribers(subreddit):
    """Return the numbers of the giving subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    try:
        results = requests.get(url=url)
        if results.status_code == 200:
            data = results.json()
            return (data['data']['subscribers'])
        else:
            return (0)
    except Exception as e:
        pass
    return (0)
