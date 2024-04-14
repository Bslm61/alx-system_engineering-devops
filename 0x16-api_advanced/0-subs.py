#!/usr/bin/python3
""" Script to obtain subscriber count from a subreddit """

import requests

def number_of_subscribers(subreddit):
    """ Function to get subscriber count """
    if subreddit and isinstance(subreddit, str):
        subscribers = 0
        url = f"https://reddit.com/r/{subreddit}/about.json"
        headers = {'user-agent': 'my-app/0.0.1'}
        try:
            req = requests.get(url, headers=headers)
            req.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
            data = req.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
        return subscribers

# Example usage:
# subreddit = 'learnpython'
# print(number_of_subscribers(subreddit))
