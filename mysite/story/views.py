from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from .models import stories
import datetime
def data_stored(request, val):
	reversed_articles = stories.objects.all().order_by('pk').reverse()[1:3]	
	story = stories.objects.get(pk=val)
	data = {'story' : story, 'recent_articles': reversed_articles}
	return render(request, 'story/story.html', data)

def show_stories(request):
	stories_titles = stories.objects.all()
	return render(request, 'story/stories.html',{'stories_T': stories_titles})
	
def show_test(request):
	return render(request, 'story/test.html')