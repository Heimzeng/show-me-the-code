from django.db import models
from django.contrib import admin
# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
    	return self.name
class Article(models.Model):
    title = models.CharField(u'标题',max_length = 150)
    content = models.TextField(u'内容')
    date = models.DateTimeField()
    tags = models.ManyToManyField(Tag, blank=True)
    def __str__(self):
    	return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    def get_tags(self):
    	return ", ".join([p.name for p in self.tags.all()])
class Updates(models.Model):
	"""docstring for Updates"""
	title = models.CharField(u'标题',max_length = 150)
	content = models.TextField(u'内容')
	date = models.DateTimeField(u'时间')
class upload_img(models.Model):
	img = models.FileField(upload_to='./upload/')
		