from django.urls import path
from .views import vocab

urlpatterns = [
    path('api/vocab/', vocab, name='vocab')
]