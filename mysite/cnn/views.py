from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.core.exceptions import PermissionDenied
from story.models import stories
from cnn.models import CategoryLinks
def index(request):
	return render(request, 'cnn/home.html')
def categories(request, val):
	if stories.objects.filter(category=val).exists():
		articles = stories.objects.filter(category=val)
		fArticles = CategoryLinks.objects.filter(category=val)
		data = {'articles':articles, 'categ': val, 'featured': fArticles}
	else:
		raise Http404('This category does not exist')
	return render(request, 'cnn/category.html', data)
def edit(request):
	articles = stories.objects.filter(category='world')
	return render(request, 'cnn/edit.html', {'articles': articles})
