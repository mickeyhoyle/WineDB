from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django import forms
from datetime import datetime
from .forms import WineForm, BottleForm
from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView, CreateView
from .models import Wine, Bottle, WineType, Country


def wine_list(request):
	wines = Wine.objects.order_by('name')
	context = {
		'wines': wines,
		# 'available_bottles': Bottle.objects.filter(available=True).count()
	}
	return render(request, 'winedb/wine_list.html', context)

def wine_detail(request, pk):
	wine = get_object_or_404(Wine, id=pk)
	bottles = wine.Bottle.all()
	context = {'wine': wine,
	'bottles': bottles}
	return render(request, 'winedb/wine_detail.html', context)


def add_new_bottle(request, pk):
	WineFormSet = inlineformset_factory(Wine, Bottle, 
		fields=('date_bought', 'bottleprice', 'available', 'drank_on'), 
		widgets= {
            'date_bought': forms.DateInput(
                attrs={'type':'date'}),
                'drank_on': forms.DateInput(
                attrs={'type':'date'}) 
        })
	wine = Wine.objects.get(id=pk)
	formset = WineFormSet(instance=wine)
	# form = BottleForm(initial={'wine':wine})
	if request.method == "POST":
		form = BottleForm(request.POST)
		if form.is_valid():
			wine = form.save(commit=False)
			wine.save()
			return redirect('/')

	context = {'formset':formset}
	return render(request, 'winedb/bottle_form.html', context)

def add_new_wine(request):
	if request.method == "POST":
		form = WineForm(request.POST)
		if form.is_valid():
			wine = form.save(commit=False)
			wine.save()
			return redirect('wine_detail', id=wine.pk)
	else:
		form = WineForm()
	return render(request, 'winedb/wine_edit.html', {'form': form})



# def bottle_count(self, obj):
# 	return obj.bottle_count

class HomeView(ListView):
	model = Wine
	template_name = 'home.html'

class WineDetailView(DetailView):
	model = Wine
	template_name = 'wine_detail.html'

