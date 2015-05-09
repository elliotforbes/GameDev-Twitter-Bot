from TwitterAPI import TwitterAPI as Twitter
from keys import codes
import time
import json


class TwitterBot():
    
    consumer_key = 'BckTYbUUHFKByssAWzrxjBg9q'
    consumer_secret = 'oVtUaw8cktkXMcNbe7Te9Ie0qBvbaDOLkCZ1DdG6uKhqlSY95X'
    access_token_key = '1937379115-p6HoW5b2xCH6Y0ktgqIYknNbwOp936M0VhFhScZ'
    access_token_secret = 'I5oHVdeOLvau7B30truWiV9zPatpSUqCJEyufyC6adP5l'
    
    
    codes = codes()
    followers = []
    api = None
    
    def __init__(self):
        self.api = Twitter(self.consumer_key, self.consumer_secret,
                          self.access_token_key, self.access_token_secret,auth_type='oAuth1')
        # Print HTTP status code (=200 when no errors).
        r = self.api.request('application/rate_limit_status')
        print(r.status_code)

    def getFollowers(self,id):
        for id in self.api.request('followers/ids', {'screen_name': id}):
            self.followers.append(id)

    def printFollowers(self):
        for user in self.followers:
            print user

    def followUsers(self):
        print("Following...")
        try:
            for follow in self.followers:
                r = self.api.request('friendships/create', {'user_id': follow})
                if r.status_code == 200:
                    status = r.json()
                    print 'Followed %s' % status['screen_name']
        except Exception as e:
            print(e)

    def promoteYoutube(self):
        print("Promoting Youtube")
        try:
            tweet = "Hey guys, check out my YouTube channel for more #GameDev tutorials, https://goo.gl/Oy5oL4"
            r = self.api.request('statuses/update', {'status': tweet})
            print r.status_code
            if r.status_code == 200:
                status = r.json()
                print 'Successfully posted'
        except Exception as e:
            print(e)    
    
if __name__ == "__main__":

    tbot = TwitterBot()
    try:
#        tbot.getFollowers("TheCherno")
#        tbot.printFollowers()
#    tbot.followUsers()
        while(1):
            tbot.promoteYoutube()
            time.sleep(6000)
    except Exception as e:
        print e
