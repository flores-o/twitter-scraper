import tweepy
import time
from secrets import *

def limit_handled(cursor):
    while True:
        try:
            yield next(cursor)
        except StopIteration:
            print("I'm dead because of some issue with python!")
            time.sleep(15 * 60)
            print("I'm back from the mess :)")
        except tweepy.RateLimitError:
            print("I'm dead :(")
            time.sleep(15 * 60)
            print("I'm back from the dead :)")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

f = open("myfile.txt", "w")
f.truncate(0)

users = []

accounts = ["pranaygp", "kirillzzy", "zrkrlc", "sjhangiani12", "PrimalNick", "raffi_hotter" ]

keywords = ["@google ", "@amazon", "@facebook", "@fb", "@microsoft", "@apple", "@stripe", "@uber", " ycs", " ycw", "@paypal", "@yahoo", "@shopify", "@instagram", "@googlemaps", "producthunt", "@palantir", "@lyft"]

for account in accounts:

  f.write("### @%s ###\n" % account)

  for page in limit_handled(tweepy.Cursor(api.followers, screen_name=account).pages()):
      print("I go to the new cursor")

      for user in page:
        bio = user.description.lower()
        
        for keyword in keywords:
          if keyword in bio:
            print(user.screen_name)
            print(bio)
            f.write("@%s\n" % user.screen_name)
            f.write("%s\n" % user.description)

      users.extend(page)

f.close()

"""
# In this example, the handler is time.sleep(15 * 60)
# but you can of course handle it in any way you want.

def limit_handled(cursor):
    while True:
        try:
            yield next(cursor)
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

for follower in limit_handled(tweepy.Cursor(api.followers).items()):
    if follower.friends_count < 300:
        print(follower.screen_name)
"""
"""
try:
    yield next(seq)
except StopIteration:
    return
 """
