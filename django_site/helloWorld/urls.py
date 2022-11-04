from django.urls imprt path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
