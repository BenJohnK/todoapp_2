from django.urls import path,include
from .views import index,update,delete


urlpatterns = [
    path('',index,name="index"),
    path('update_task/<int:pk>/',update,name="update_task"),
    path('delete_task/<int:pk>',delete,name="delete_task")
]