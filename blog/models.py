from django.db import models

# Create your models here.


class Blog(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=200)
	content = models.TextField(null=True, blank=True)
	short_desc = models.CharField(max_length=250, default="", null=True, blank=True)
	slug = models.CharField(max_length=100)
	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

