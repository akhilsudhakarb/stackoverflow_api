from django.urls import path,include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('questions', views.QuestionApi)

urlpatterns = [
    # path('', views.index),
    path('', include(router.urls)),
    path('latest', views.QuestionApi.latest, name='latest'),
]