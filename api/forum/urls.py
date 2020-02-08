from django.conf.urls import url, include
from rest_framework_nested import routers
from forum.views import ForumViewset

forum = routers.SimpleRouter()

forum.register(
    r'forum',
    ForumViewset,
    base_name='Forum operations'
)

urlpatterns = [
    url(r'^', include(forum.urls)),
    
]