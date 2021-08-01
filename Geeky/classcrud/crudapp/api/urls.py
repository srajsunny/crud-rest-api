from django.urls import path, include
from crudapp.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('yoyo', views.UserModelViewSet,basename='user')


urlpatterns=[
    path('',include(router.urls))
]