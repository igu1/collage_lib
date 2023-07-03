from django.urls import path
from .views import *
urlpatterns = [
    path('cron/', Cron.as_view() , name='cron'),
]
