from django.urls import path, register_converter
from menu import views, converts


register_converter(converts.ListConverter, 'list')
urlpatterns = [
    path('', views.index, name='home'),
    path('<list:menu_url>/', views.menu, name='menu_name')
]