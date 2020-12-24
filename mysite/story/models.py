from django.db import models

class stories(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField()
	author = models.CharField(max_length=30)
	date_posted = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(default = 'media/def.jpeg', upload_to='media')
	category = models.CharField(blank=True, default='world', max_length=75)
	def __str__(self):
		return self.title