from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # home에서 views.post_list 보여줌, url name 설정
]