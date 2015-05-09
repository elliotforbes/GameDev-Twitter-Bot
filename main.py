from TwitterAPI import TwitterAPI
 
#enter the corresponding information from your Twitter application:
consumer_key = 'BckTYbUUHFKByssAWzrxjBg9q'#keep the quotes, replace this with your consumer key
consumer_secret = 'oVtUaw8cktkXMcNbe7Te9Ie0qBvbaDOLkCZ1DdG6uKhqlSY95X'#keep the quotes, replace this with your consumer secret key
access_token_key = '1937379115-p6HoW5b2xCH6Y0ktgqIYknNbwOp936M0VhFhScZ'#keep the quotes, replace this with your access token
access_token_secret = 'I5oHVdeOLvau7B30truWiV9zPatpSUqCJEyufyC6adP5l'#keep the quotes, replace this with your access token secret

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = api.request('search/tweets', {'q':'gamedev'})
for item in r:
        print item
        
print('\nQUOTA: %s' % r.get_rest_quota())