from django.urls import path
from .views import ScrapView, home

app_name = 'scrapper'
urlpatterns = [
    # path('index/', views.scrap, name='index'),
    path('scrap/', ScrapView.as_view(), name='scrap'),
    path('home/', home, name='home'),
]