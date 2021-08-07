from django.db import models

# Create your models here.
class Test(models.Model):
	name = models.CharField(max_length=40, verbose_name='Test name')
	author = models.CharField(max_length=300)
	questionsAndAnswers = models.CharField(max_length=1000)
	result = models.CharField(max_length=1000, default='Nope')
	answers = models.CharField(max_length=1000, default='0')


	def __str__(self):
		return self.name