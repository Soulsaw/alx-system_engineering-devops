#!/usr/bin/python3
"""API Advanced"""
import requests


def top_ten(subreddit):
    """Return the 10 hot comments"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    try:
        results = requests.get(url=url)
        if results.status_code == 200:
            data = results.json()
            for comment in data['data']['children'][:10]:
                print(comment['data']['title'])
            return
    except Exception as e:
        pass
    print(None)
