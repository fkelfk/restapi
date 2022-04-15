# from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from addresses import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('addresses/', views.addresses_list),
    path('addresses/<int:pk>/', views.address),
    path('login/', views.login),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
