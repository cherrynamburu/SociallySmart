import logging
import re

from django.conf import settings
from django.utils import timezone
# from .models import Story

import requests
#from bs4 import BeautifulSoup

# logger = logging.getLogger(__name__)

# class AbstractBaseClient:
#     """Base class which holds the header name """
#     def __init__(self):
#         self.headers = {'user-agent': 'socially-smart/1.0'}


"""Returns a list of reddit stories """
def get_front_page_stories():

    stories = list()

    r = requests.get('https://reddit.com/.json',headers = {'user-agent': 'socially-smart/1.0'})
    result = r.json()
    stories = result['data']['children']     # Returns the children tag from reddit.json() file which contains data we need

    # logger.exception('An error occurred while executing RedditClient.get_front_page_stories')

    return stories

class RedditCrawler():
    # def __init__(self):
    #     super().__init__('reddit', RedditClient())

    def update_top_stories(self):
        stories = get_front_page_stories()
        for data in stories:

            story_data = data['data']

            # comments = story_data.get('num_comments', 0)
        #     story = Story.objects.get_or_create(code=story_data.get('permalink'))
        #     story.build_url()
        #
        #     print(comments)
        #     print(code)
        #
        #     story.title = story_data.get('title', '')
        #     story.comments = comments
        #     story.save()
            # print(comments)
            return story_data

#
# obj = RedditCrawler()
# obj.update_top_stories()


# class AbstractBaseCrawler:
#     def __init__(self, slug, client):
#         #self.service = Service.objects.get(slug = slug)
#         self.slug = slug
#         self.client = client
