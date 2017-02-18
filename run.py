#!/usr/bin/env python

from os import environ

try:
    C_KEY = environ['C_KEY']
    C_SECRET = environ['C_SECRET']
    A_TOKEN = environ['A_TOKEN']
    A_TOKEN_SECRET = environ['A_TOKEN_SECRET']
except KeyError:
    print('Credentials error: You need to set your Twitter keys in .env, then run "source .env"')
    exit(1)

# here's some example usage
if __name__ == '__main__':
    from pruner import TweetPruner

    pruner = TweetPruner(C_KEY, C_SECRET, A_TOKEN, A_TOKEN_SECRET)

    # the max_show parameter determines how many accounts you want to list
    # feel free to show more/less, or remove the argument to see everything
    pruner.show_worst_offenders(max_show=30)

    # the keyword parameter limits this to only look at tweets containing a keyword
    # you can change this to whatever you're seeing too much of
    pruner.show_worst_offenders(keyword='trump')
