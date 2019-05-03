from django.db import models

class Tweets(models.Model):
    '''Models Twitter tweet data.'''
    id = models.IntegerField(primary_key=True)
    screen_name = models.CharField(max_length=200)
    tweet_id = models.IntegerField()
    created_at = models.DateTimeField()
    source = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    favorite_count = models.IntegerField()
    retweet_count = models.IntegerField()

class Trends(models.Model):
    '''Models Twitter trending data.'''
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    tweet_volume = models.IntegerField()





