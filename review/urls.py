from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.review_view, name="home"),
    path('new_review', views.new_review, name="new_review"),
    path('update_review/<int:review_id>', views.update_review, name="update_review"),
]