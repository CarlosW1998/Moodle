from django.conf.urls import url, include
from rest_framework_nested import routers
from posts.views import PostsViewset

posts = routers.SimpleRouter()

posts.register(
    r'posts',
    PostsViewset,
    base_name='Posts operations'
)

urlpatterns = [
    url(r'^', include(posts.urls)),
    
]