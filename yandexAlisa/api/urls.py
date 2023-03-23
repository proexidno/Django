from django.urls import path, include

from api.views import index

from .views import index

urlpatterns = [
    path('', index),
    path('/cryptoAdvisor', include('cryptoAdvisor.urls')),
]
