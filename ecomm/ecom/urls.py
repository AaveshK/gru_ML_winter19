#Django imports
from django.urls import path

#app level imports
from ecom import views

urlpatterns = [
    path('',views.func_view)
]