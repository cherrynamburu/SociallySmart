from django.urls import path, include
from onion import views

urlpatterns = [
    path('scrape/', views.scrape, name = 'scrape_onion'),
    path('',views.news_list, name='home'),
]
