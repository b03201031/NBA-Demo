from django.shortcuts import render

from .serializers import NBANewsSerializer 
from .models import NBANews

from rest_framework import viewsets

# Create your views here.


class NBANewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NBANews.objects.all()
    serializer_class = NBANewsSerializer

def news_list(request):
    context = {
        'url': "http://127.0.0.1:8000/nba/api/news/",
    }
    return render(request, 'news/list.html', context=context)

def news_detail(request, news_id):
    context = {
        'url': "http://127.0.0.1:8000/nba/api/news/",
        'id': news_id,
    }
    return render(request, 'news/detail.html', context=context)