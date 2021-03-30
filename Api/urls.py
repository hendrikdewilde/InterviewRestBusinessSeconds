# from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from Api import views
# from api.views_auth_token import obtain_auth_token_custom

router = routers.DefaultRouter()
router.register(r'business_seconds', views.BusinessSecondsViewSet, basename='BusinessSeconds')


urlpatterns = [
    re_path(r'^', include(router.urls)),
]
