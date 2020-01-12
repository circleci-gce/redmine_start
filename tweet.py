# coding:utf-8

import os
import sys
import tweepy

args = sys.argv

# Create twitter objects
auth = tweepy.OAuthHandler(args[1], args[2])
auth.set_access_token(args[3], args[4])
api = tweepy.API(auth)

# Create message body
URL = os.environ['CIRCLE_BUILD_URL']
REDMINE_IP = os.environ['REDMINE_IP']

message = 'CircleCI started an VM instance' + '\n\n' \
          'http://' + REDMINE_IP + '/redmine' + '\n\n' \
          + URL

api.send_direct_message(args[5], message)
