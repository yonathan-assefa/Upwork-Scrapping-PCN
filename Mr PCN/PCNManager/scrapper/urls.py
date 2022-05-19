from django.urls import path
from .views import ScrapView, FillEmailView, home, PCNListView, generate_pdf


app_name = 'scrapper'
urlpatterns = [
    path('scrap/', ScrapView.as_view(), name='scrap'),
    path('fill-email/', FillEmailView.as_view(), name='fillemail'),
    path('', home, name='home'),

    path('pcn-list/', PCNListView.as_view(), name='pcnlist'),
    path('generate-pdf/', generate_pdf, name='generatepdf'),
]