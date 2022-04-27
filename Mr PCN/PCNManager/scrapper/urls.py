from django.urls import path
from .views import ScrapView, FillEmailView, home


app_name = 'scrapper'
urlpatterns = [
    path('scrap/', ScrapView.as_view(), name='scrap'),
    path('fill-email/', FillEmailView.as_view(), name='fillemail'),
    path('home/', home, name='home'),
]