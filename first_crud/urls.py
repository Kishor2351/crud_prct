
from django.urls import path
from .views import *

urlpatterns = [
    path('school/', SchoolApiView.as_view(), name='school'),
    path('school/<int:id>', SchoolApiView.as_view(), name='school'),
    path('student/', StudentAPIView.as_view(), name='student'),
    path('student/<int:id>', StudentAPIView.as_view(), name='student')
]
