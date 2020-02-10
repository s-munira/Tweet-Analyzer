from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import twitter_credentials

import json
# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list,languages=['en'])


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            with open(self.fetched_tweets_filename, 'a') as tf:
                json_load= json.loads(data)
                text=json_load['text']
                tf.write(json.dumps(text))   
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
   # Authenticate using config.py and connect to Twitter Streaming API.
   hash_tag_list = ["Add-on Security","Advanced Encryption Standard ","Advanced Key Processor", "Advanced Persistent Threats","Adversary", "Antispyware Software", "Antivirus Software", "Authentication ", "Biometric System","Blended Attack", "Block Cipher", "Block","Disclose","password","hack","cybercrime","identity theft","facebook","tweeter",
					 "text","privacy","safety","unfriend","suspicious","security","message","IP","dns","compromised","breach","border"]
   fetched_tweets_filename = "tweets.json"

   twitter_streamer = TwitterStreamer()
   twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

          
 


