

from django.contrib import admin
from django.urls import path,include
from todolist import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name="index"),
    path('task/',include('todolist.urls'),name="task"),
    path('account/',include('xanre_users.urls'),name="account"),
    path('contact',views.contact,name="contact"),
    path('about',views.about, name="about"),
]
