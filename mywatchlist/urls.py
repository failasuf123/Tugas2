from urllib.parse import urlparse
from django import urls
from django.urls import URLPattern, path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_xml
from mywatchlist.views import show_json
from mywatchlist.views import show_json_by_id

app_name = "mywatchlist"

urlpatterns = [
    path('html/', show_mywatchlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]