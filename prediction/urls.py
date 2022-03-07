from django.urls import path
from .views import prediction

urlpatterns = [
    path('api/prediction/', prediction, name='prediction')
]