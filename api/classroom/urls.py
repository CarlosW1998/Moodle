from django.conf.urls import url, include
from rest_framework_nested import routers
from classroom.views import ClassroomViewset

classroom = routers.SimpleRouter()

classroom.register(
    r'classroom',
    ClassroomViewset,
    base_name='Classroom operations'
)

urlpatterns = [
    url(r'^', include(classroom.urls)),
    
]