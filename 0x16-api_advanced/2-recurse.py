#!/usr/bin/python3
"""API Advanced"""
import requests


def recurse(subreddit, hot_list=[]):
    if len(hot_list) >= 100:
        return hot_list
    """Return the 10 hot comments"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    try:
        results = requests.get(url=url)
        if results.status_code == 200:
            data = results.json()
            for comment in data['data']['children']:
                hot_list.append(comment['data']['title'])
            if data['data']['after'] is not None:
                recurse(subreddit, hot_list=hot_list)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        pass
    return (None)
