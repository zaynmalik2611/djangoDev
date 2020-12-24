from django.db import models

class CategoryLinks(models.Model):
	category = models.CharField(blank=True, default='world', max_length=75)
	title = models.CharField(max_length=150)
	image = models.ImageField(default = 'media/def.jpeg', upload_to='media')
	desc = models.TextField()
	serialNo = models.IntegerField()
	def __str__````(self):
		return self.category