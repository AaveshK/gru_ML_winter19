"""ecomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#django imports
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

#rest_framework imports
from rest_framework import routers

#app level imports
from ecom.views import ProductView
from ecom.views import ClothingView
from ecom.views import ElectronicsView
from ecom.views import BooksView
from ecom.views import SportsView
from ecom.views import KitchenView

router = routers.DefaultRouter()

router.register('Product', ProductView)
router.register('Clothing', ClothingView)
router.register('Electronics', ElectronicsView)
router.register('Books', BooksView)
router.register('Kitchen', SportsView)
router.register('Sports', KitchenView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls'))
]




'''class ThisWillBeTheApiTitleView(routers.APIRootView):
    """
    This appears where the docstring goes!
    """
    pass


class DocumentedRouter(routers.DefaultRouter):
    APIRootView = ThisWillBeTheApiTitleView


router = DocumentedRouter()'''
