from django.urls import path
from .views import GetInfos, post_form

urlpatterns = [
    path('', GetInfos.as_view()),
    path('submit/', post_form, name='post_form')
]