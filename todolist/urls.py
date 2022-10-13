
import imp
from django.urls import path
from todolist.views import show_todolist
from todolist.views import signup_user
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_task
from todolist.views import show_json
from todolist.views import show_json_by_id


app_name = "todolist"

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('task/', create_task, name='create_task'),
    path('signup/', signup_user, name='signup_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'), 
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
]