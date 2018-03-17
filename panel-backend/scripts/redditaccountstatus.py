#!/usr/bin/env python3
import praw
import time
import passwords
import panelconfig
reddit = praw.Reddit(client_id='t7q7A6sYFM2Tgw',
                     client_secret='YOIkt2oi_3RdoRbPUuBWYjlCNyE',
                     password=passwords.reddit_password,
                     user_agent='redditscript',
                     username='Makefile_dot_in')
def lemonbar():
    message_count = len(list(reddit.inbox.unread()))
    return (message_count, reddit.user.me().comment_karma + reddit.user.me().link_karma)

while True:
    returned = [str(x) for x in lemonbar()]
    with open(panelconfig.configdir + '/ipc/reddit_msgcount', 'w') as f:
        f.write(returned[0])
    with open(panelconfig.configdir + '/ipc/reddit_karma', 'w') as f:
        f.write(returned[1])
    time.sleep(5)
