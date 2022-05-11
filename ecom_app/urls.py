from django.urls import path
from django import views
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('post/<int:pk>/delete',BlogDeleteView.as_view(),name="post_delete"),
    path('post/<int:pk>/edit',BlogUpdateView.as_view(),name="post_edit"),
    path('post/new/', CreateView.as_view(), name="post_new"),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_details'),
    path('',BlogView.as_view(),name='BlogView'),
   
]

urlpatterns += staticfiles_urlpatterns()