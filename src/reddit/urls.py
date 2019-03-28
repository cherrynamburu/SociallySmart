from django.urls import path, include
from reddit import views

urlpatterns = [
    path('scrape/', views.scrape_reddit, name = 'scrape_reddit'),
]
