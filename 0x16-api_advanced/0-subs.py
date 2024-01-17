#!/usr/bin/python3
"""API Advanced"""
import requests


def number_of_subscribers(subreddit):
    """Return the numbers of the giving subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    results = requests.get(url=url, allow_redirects=False)
    if results.status_code == 200:
        data = results.json()
        return (data['data']['subscribers'])
    else:
        return (0)
