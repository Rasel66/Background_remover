from django.urls import path
from .views import *

urlpatterns = [
    path('', upload_image_view, name='upload_image'),
    path('result/<int:pk>/', result_view, name='result')
]
