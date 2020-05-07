# 0x16. API advanced

## General
* How to read API documentation to find the endpoints you’re looking for
* How to use an API with pagination
* How to parse JSON results from an API
* How to make a recursive API call
* How to sort a dictionary by value

## 0. How many subs? 
function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Example

    wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
    756024
    wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
    0

## 1. Top Ten
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
