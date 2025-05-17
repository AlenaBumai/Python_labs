from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Topic, NewsText


def index(request):
    topics = Topic.objects.all()
    return render(request, "index.html", {'topics': topics})

def newstext(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    news_texts = topic.newstext_set.all()  # Получаем все связанные тексты новостей
    return render(request, "newstext.html", {'topic': topic, 'news_texts': news_texts})
def contacts(request):
    return render(request, "contacts.html")