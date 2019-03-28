import requests
import logging
from django.conf import settings


logger = logging.getLogger(__name__)

class AbstractBaseClient:
    """Base class which holds the header name """
    def __init__(self):
        self.headers = {'user-agent': 'socially-smart/1.0'}


class RedditClient(AbstractBaseClient):

    def get_front_page_stories(self):
        """Returns a list of reddit stories """
        stories = list()

        try:
            r = requests.get('https://reddit.com/.json',headers = self.headers)
            result = r.jason()
            stories = result['data']['children']     # Returns the children tag from reddit.json() file which contains data we need
        except ValueError:
            logger.exception('An error occurred while executing RedditClient.get_front_page_stories')

        return stories
