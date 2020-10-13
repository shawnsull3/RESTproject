from django.urls import path
from myapi import views 
 
urlpatterns = [ 
    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]