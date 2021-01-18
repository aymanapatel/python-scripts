# Trying out APIs which will be used in `twitter-api.py`
import click
import tweepy
import click

###### Credentials
# consumer_key
# consumer_token
# access_token
# access_token_secret
######


def authenticate_and_authorize_return_api_object():

    consumer_key = ""
    consumer_secret = ""

    access_token = ""
    access_token_secret = ""
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    return api

"""
`python3 twitter_trial.py -help` 
OR
`python3 twitter_trial.py --help`
"""
@click.command()
#@click.option('--count', default=1, help='Number of greetings.')
@click.option('-n', '--name', help='Twitter username', is_flag=True)
@click.option('-l', '--lists', help='List', is_flag=True)
def click_cli(name, lists):

    api = authenticate_and_authorize_return_api_object()
    
    
    if (name):
        user = api.me()
        click.echo('Hello @%s!' % user.screen_name)

    if (lists):
        lists = api.list_timeline(list_id = 1346079189942747136)

        for tweet in lists:
            click.echo('User: %s' % tweet.user.screen_name)    
            click.echo('Tweet: %s' % tweet.text)    

if __name__ == '__main__':

    click_cli()
    
    
