from django.urls import include, path
from myapi import views 
 
urlpatterns = [ 
    path('users/', views.users_list),
    path('users/<int:pk>/', views.user_detail),
]