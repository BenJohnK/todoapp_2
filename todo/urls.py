from django.urls import path,include
from .views import index,update


urlpatterns = [
    path('',index,name="index"),
    path('update_task/<int:pk>/',update)
]