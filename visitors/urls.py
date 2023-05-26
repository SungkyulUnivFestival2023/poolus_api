from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', VisitorsView.as_view()),
    # path('counts/', CountView),
]
