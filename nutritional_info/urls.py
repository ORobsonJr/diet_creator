from django.urls import path
from .views import GetInfos, post_form, get_receipes

urlpatterns = [
    path('', GetInfos.as_view()),
    path('submit/', post_form, name='post_form'),
    path('submit/receipes/', get_receipes, name='get_receipes')
]