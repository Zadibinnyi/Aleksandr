from django.db import models

class Download(models.Model):
	data = models.DateTimeField(auto_now_add=True),
	name = models.CharField(max_length=100),
	size = models.PositiveIntegerField(),
	file = models.FileField(upload_to='file')
    

	def __str__(self):
		return self.name
