from django.contrib import admin
from django.db import models
from django.db.models import Q, Count
from .models import *
from django.forms import SelectMultiple, CheckboxSelectMultiple
from django.contrib.admin.widgets import AutocompleteSelect


	
class BottleInline(admin.TabularInline):
	model = Bottle
	extra = 0	



class WineAdmin(admin.ModelAdmin):
	list_display = ['producer', 'name', 'bottle_count', 'available_bottle']
	formfield_overrides = {
		models.ManyToManyField: {'widget': CheckboxSelectMultiple},

	}
	inlines = [BottleInline]
	fields = (
        'producer', 
        'name',
        'year',
        'grape',
        'colour',
        'alcohol',
        'wine_type',
        'notes',
        
    )
	
    
	def save_model(self, request, obj, form, change):
		obj.author = request.user
		super().save_model(request, obj, form, change)

	

	def get_form(self, request, obj=None, **kwargs):

		request._obj_ = obj
		return super(WineAdmin, self).get_form(request, obj, **kwargs)

	def bottle_count(self, obj):
		return obj.bottle_count

	def get_queryset(self, request):
		queryset = super().get_queryset(request)
		queryset = queryset.annotate(bottle_count=Count("Bottle"))
		return queryset





admin.site.register(Wine, WineAdmin)
admin.site.register(Bottle) 
admin.site.register(WineType) 
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Colour)
admin.site.register(Producer)
admin.site.register(Grape)




