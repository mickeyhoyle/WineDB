from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib import admin
from django.forms import ModelForm


COLOUR = [
    ('-', '-'),
    ('White', 'White'),
    ('Orange', 'Orange'),
    ('Red', 'Red'),
    ('Rose', 'Rose'),
    ('Pet Nat', 'Pet Nat'),
    
]

class Country(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name

class Colour(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name


class Region(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name

class Grape(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.name

class WineType(models.Model):
	referring_wine_type = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.referring_wine_type

class Producer(models.Model):
	referring_producer_name = models.CharField(max_length=200, blank=True, null=True)
	referring_producer_country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE)
	referring_producer_region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)


	def __str__(self):
		return self.referring_producer_name


class Wine(models.Model):
	producer = models.ForeignKey(Producer, null=True, blank=True, on_delete=models.CASCADE, default=0)
	name = models.CharField(max_length=200)
	year = models.IntegerField(blank=True, null=True)
	alcohol = models.IntegerField(blank=True, null=True)
	grape = models.ForeignKey(Grape, null=True, blank=True, on_delete=models.CASCADE, default=0)
	colour = models.ForeignKey(Colour, null=True, blank=True, on_delete=models.CASCADE, default=0)
	wine_type = models.ForeignKey(WineType, null=True, blank=True, on_delete=models.CASCADE, default=0)
	notes = models.TextField(max_length=2000, blank=True, null=True)
	

	def __str__(self):
		return self.name


	def get_bottles(self):
		a = []
		for bottle in self.Bottle.all():
			a.append((bottle.date_bought))

		return a

	def available_bottle(self):
		number = self.Bottle.filter(available=True).count()
		return number


class Bottle(models.Model):
	wine = models.ForeignKey(Wine, related_name='Bottle', on_delete=models.CASCADE)
	date_bought = models.DateField(blank=True, null=True)
	bottleprice = models.CharField(max_length=200, blank=True,)
	#notes = models.TextField(max_length=2000, blank=True, null=True)
	available = models.BooleanField(default=True)
	drank_on = models.DateField(blank=True, null=True)

	

	def __str__(self):
		return str(self.date_bought)
		
	def save(self, *args, **kwargs):
		if self.drank_on is not None:
			self.available=False

		super(Bottle, self).save(*args, **kwargs)

	

		

