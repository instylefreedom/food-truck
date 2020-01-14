from django.db import models

class Truck(models.Model):
	name = models.CharField(max_length=200)
	menu = models.CharField(max_length=200)

	def __str__(self):
		return self.name + ': ' + self.menu

class order(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name