from django.urls import path,include
from app.views_api import UserViewSet
from . import views
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

app_name='app'
urlpatterns = [
     path('api-auth/', include('rest_framework.urls')),
     #path('',include(router.urls)),
     path('users/',views.users_list),
]