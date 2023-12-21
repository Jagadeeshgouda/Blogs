from . import views
from django.urls import path

from .views import (
    BlogPostListCreateAPIView,
    BlogPostDetailAPIView,
    BlogContentListCreateAPIView,
    BlogContentDetailAPIView,
)

urlpatterns = [
    path('add/',views.create_blog),
    path('newuser',views.createUser),
    path('',views.login_form),
    path('logout',views.logout_form),
    path('changepassword',views.changepassword),
    path('verify/',views.verifyUser,name="verify"),
    path('success/',views.success,name="success"),
    path('blogposts/', BlogPostListCreateAPIView.as_view(), name='blogpost-list'),
    path('blogposts/<int:pk>/', BlogPostDetailAPIView.as_view(), name='blogpost-detail'),
    path('blogcontent/', BlogContentListCreateAPIView.as_view(), name='blogcontent-list'),
    path('blogcontent/<int:pk>/', BlogContentDetailAPIView.as_view(), name='blogcontent-detail'),
]
