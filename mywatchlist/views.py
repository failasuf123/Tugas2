from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

data_list = MyWatchList.objects.all()

context = {
    'name' : 'Failasuf Indi Marsendy',
    'npm' : '2106750364',
    'mylist': data_list,
}

# Create your views here.
def show_mywatchlist(request):
    return render(request, "mywatchlist.html",context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

#json
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# return data id
def show_json_by_id(request, id):
    data =  MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    # return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")