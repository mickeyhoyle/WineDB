from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import WineForm
from django.views.generic import ListView, DetailView, CreateView
from .models import Wine, Bottle, WineType, Country


def wine_list(request):
	wines = Wine.objects.order_by('name')
	context = {
		'wines': wines,
		# 'available_bottles': Bottle.objects.filter(available=True).count()
	}
	return render(request, 'winedb/wine_list.html', context)

def wine_new(request):
	form = WineForm()
	return render(request, 'winedb/wine_edit.html', {'form': form})

def wine_detail(request, pk):
	wine = get_object_or_404(Wine, pk=pk)
	bottles = wine.Bottle.all()
	context = {'wine': wine,
	'bottles': bottles}
	return render(request, 'winedb/wine_detail.html', context)


# def bottle_count(self, obj):
# 	return obj.bottle_count

class HomeView(ListView):
	model = Wine
	template_name = 'home.html'

class WineDetailView(DetailView):
	model = Wine
	template_name = 'wine_detail.html'

