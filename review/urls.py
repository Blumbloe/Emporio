from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home_view, name="home"),
    path('new_review', views.new_review, name="new_review"),
    path('review_list', views.review_list, name="review_list"),
    path('update_review/<int:review_id>', views.update_review, name="update_review"),
    path('delete_review/<int:review_id>', views.delete_review, name="delete_review"),
]