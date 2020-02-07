from django.conf.urls import url, include
from rest_framework_nested import routers
from users.views import AuthVeiwset

Auth_router = routers.SimpleRouter()

Auth_router.register(
    r'users',
    AuthVeiwset,
    base_name='Clients Auths'
)

urlpatterns = [
    url(r'^', include(Auth_router.urls)),
    
]