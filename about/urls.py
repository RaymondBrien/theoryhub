from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.About.as_view(), name='about'), # class based view TODO: make basic about view
]