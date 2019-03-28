from django.shortcuts import render, redirect
import requests
from .models import Story

# Create your views here.

"""Returns a list of reddit stories """
def get_reddit_stories():
    stories = list()

    # sending the request with data inserted.
    r = requests.get('https://reddit.com/.json',headers = {'user-agent': 'socially-smart/1.0'})

    # Converting the data we got to json format
    result = r.json()

    # Returns the children tag from reddit.json() file which contains data we need
    stories = result['data']['children']
    return stories

def get_top_three_posts():
    redditDict = {}
    stories = Story.objects.all()
    for each in stories:
        redditDict[each.comments] = each;
    #print(sorted(redditDict))
    for i in sorted(redditDict) :
        print(i, redditDict[i])


def scrape_reddit(request):
    #deleting all the reddit posts in the database
    Story.objects.all().delete()

    # Get the stories from the reddit.com website
    stories = get_reddit_stories()



    # Loop through the list of posts  we gathered
    for data in stories:

        # Retreiving the actual data of the post
        story_data = data['data']

        # Creating the database instance to write data to the database
        story = Story()

        # write the data we got into the object
        story.code = story_data.get('permalink')

        #Bulding the url From the code data
        story.build_url()

        comments = story_data.get('num_comments', 0)

        story.title = story_data.get('title', '')
        story.comments = comments
        story.save()
        #get_top_three_posts()


    return redirect('home')
