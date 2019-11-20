from django.urls import path
from mart import views

urlpatterns = [
    path('', views.index, name='index'),
    path('order', views.create_order, name='create_order'),
    path('order/<int:pk>/', views.delete_order, name='delete_order'),
]
