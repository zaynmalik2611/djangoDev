from django.contrib import admin
from .models import stories
from cnn.models import CategoryLinks

admin.site.register(stories)
admin.site.register(CategoryLinks)