from django.urls import path
from . import views

app_name = "catalogue"

urlpatterns = [
    path('tees/', views.cat1, name="tees"),
    path('hoodies_sweater/', views.cat2, name="hoodies_sweater"),
    path('pants/', views.cat3, name="pants"),
    path('exclusive_apparel/', views.cat4, name="exclusive_apparel")
]
