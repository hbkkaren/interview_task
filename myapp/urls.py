
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path('clear',views.clear, name= "clear"),
    path('delete_order/<int:pk>/',views.delete_order, name= "delete_order"),
    path('update_order/<int:pk>/',views.update_order, name= "update_order"),
    path('update_profile/<int:pk>/',views.update_profile, name= "update_profile"),
   
]
