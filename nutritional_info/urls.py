from django.urls import path
from .views import GetInfos

urlpatterns = [
    path('', GetInfos.as_view())
]