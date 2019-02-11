from django.shortcuts import render, redirect
from django.conf import settings
import requests
requests.packages.urllib3.disable_warnings()
import os, shutil
from bs4 import BeautifulSoup
from .models import Headline


def news_list(request):
    headlines = Headline.objects.all()
    context = {
        'object_list':headlines
    }
    return render(request, "onion/home.html",context)


def scrape(request):

    session = requests.Session()
    session.headers= {'User-Agent':"Mozilla/5.0"}
    url = 'https://www.theonion.com/'

    content = session.get(url,verify=False).content
    soup = BeautifulSoup(content, "html.parser")

    posts = soup.find_all('div',{'class':'curation-module__item'})

    for i in posts[:3]:
        link = i.find_all('a',{'class':'js_curation-click'})[1]['href']
        title = i.find_all('a',{'class':'js_curation-click'})[1].text
        image_source = i.find('img',{'class':'featured-image'})['data-src']

        media_root = settings.MEDIA_ROOT
        if not image_source.startswith(("data:image", "javascript")):
            local_filename = image_source.split('/')[-1].split('?')[0]
            r = session.get(image_source,stream = True, verify=False)
            with open(local_filename,'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
            current_image_obsolute_path = os.path.abspath(local_filename)
            shutil.move(current_image_obsolute_path, media_root)


        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = local_filename
        new_headline.save()

    return redirect('list')
