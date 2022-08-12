from email.policy import default
from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path , include
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('address',AdressViewset)


urlpatterns=[

    path ('api/', include(router.urls))
]