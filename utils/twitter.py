# twitter.py
import sys

import tweepy
import os
import dotenv
import datetime
from datetime import datetime, timedelta
dotenv.load_dotenv()

# Load the Twitter API token from the .env file
api_token = os.getenv("TWITTER_API_TOKEN")

# Authenticate with the tweepy API using the bearer token
auth = tweepy.OAuth2BearerHandler(api_token)
api = tweepy.API(auth)
client = tweepy.Client(api_token)


def get_thread(thread_id):
    # Fetch the thread using the tweepy API
    thread = client.get_tweet(thread_id, expansions="attachments.media_keys,author_id,referenced_tweets.id,referenced_tweets.id.author_id", tweet_fields='conversation_id,created_at')
    # Check if it has been less than a week since thread was created
    older_thread = thread.data.get('created_at').astimezone() > datetime.now().astimezone() - timedelta(weeks=1)


    # Initialize an empty list to store the replies
    replies = []

    # Iterate over all the replies to the initial tweet that belong to the original author of the thread
    conversation = client.search_recent_tweets(query=f"conversation_id:{thread.data.get('conversation_id')} -is:retweet", expansions="attachments.media_keys,author_id,referenced_tweets.id,referenced_tweets.id.author_id", tweet_fields='conversation_id', max_results=100, sort_order="recency")
    for reply in conversation:
        # Add the reply to the list of replies
        replies.append(reply.text)

    # Concatenate all the replies into 1 coherent text
    text = "\n".join(replies)
    return text


if __name__ == "__main__":
    thread_id = sys.argv[1]
    top_quote_tweets = get_thread(thread_id)
    print(top_quote_tweets)

