from django.db import models
from django.utils import timezone

class Post(models.Model):
	author=models.ForeignKey('auth.User')
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_on=models.DateTimeField(default=timezone.now)
	published_on=models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_on=timezone.now()
		self.save()

	def _str_(self):
		return self.title
