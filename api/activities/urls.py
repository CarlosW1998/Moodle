from django.conf.urls import url, include
from rest_framework_nested import routers
from activities.views import ActivityViewsets, AnswerViewset
answer = routers.SimpleRouter()
activity = routers.SimpleRouter()
answer.register(
    r'answer',
    AnswerViewset,
    base_name='Answer operations'
)
activity.register(
    r'activity',
    ActivityViewsets,
    base_name='Activity Operations'
)

urlpatterns = [
    url(r'^', include(answer.urls)),
    url(r'^', include(activity.urls)),   
]