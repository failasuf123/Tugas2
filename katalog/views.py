from django.shortcuts import render
from katalog.models import CatalogItem

data_katalog = CatalogItem.objects.all()
context = {
    'name' : 'Failasuf Indi Marsendy',
    'npm' : '2106750364',
    'list_katalog': data_katalog,
}

# TODO: Create your views here.
def show_katalog(request):
    return render(request, "katalog.html",context)

