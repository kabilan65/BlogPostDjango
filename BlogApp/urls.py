from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post_detail/<int:pk>', views.post_detail, name="post_detail"),
    path('post_edit/<int:pk>', views.post_edit, name="post_edit"),
    path('post_delete/<int:pk>', views.post_delete, name="post_delete"),
    path('delete_comment/<int:pk>', views.delete_comment, name="delete_comment"),
    path('search_post/', views.search_post, name='search_post'),
]