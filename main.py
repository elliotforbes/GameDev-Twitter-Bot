from TwitterAPI import TwitterAPI
 
#enter the corresponding information from your Twitter application:
consumer_key = 'Pisuo7SzAMx4oFKviIyutpjum'#keep the quotes, replace this with your consumer key
consumer_secret = 'TmG10F6fzW83k30ktV34i7Ig6rH1VlJdVSpM9ADVHjfGSrJaTY'#keep the quotes, replace this with your consumer secret key
access_token_key = '1937379115-p6HoW5b2xCH6Y0ktgqIYknNbwOp936M0VhFhScZ'#keep the quotes, replace this with your access token
access_token_secret = 'I5oHVdeOLvau7B30truWiV9zPatpSUqCJEyufyC6adP5l'#keep the quotes, replace this with your access token secret

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = api.request('search/tweets', {'q':'gamedev'})
for item in r:
        print item
        
print('\nQUOTA: %s' % r.get_rest_quota())