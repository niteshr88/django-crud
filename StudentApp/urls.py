from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from StudentApp import views


urlpatterns = [
    path('', views.index),
    path('show/', views.show, name="edit"),
    path('show/update/<str:email>', views.edit),
    path('update', views.update),
    path('show/delete/<str:email>', views.delete),
    path('display', views.display),
    path('user', views.user),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
