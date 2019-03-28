from django.shortcuts import render, redirect
from reddit.models import Story
from onion.models import Headline

def sortthings():
    stories = Story.objects.all()
    redditDict = {}
    count = 3
    for each in stories:
        #print(each)
        redditDict[each.comments] = each
    #print(stories)
    Story.objects.all().delete()

    for i in sorted(redditDict, reverse = True):
        if count:
            story = Story()
            story =  redditDict[i]
            story.save()
            count = count - 1



def home(request):
    stories = Story.objects.all()
    headlines = Headline.objects.all()
    if(len):
        sortthings()
    context = {
        'reddit_list' : stories,
        'onion_list':headlines,

    }
    return render(request, "home.html", context)
