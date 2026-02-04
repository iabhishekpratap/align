from django.urls import path
from . import views

app_name = 'task_list'

urlpatterns = [
    path('', views.login_page, name='login'),
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('register/', views.register_page, name='register'),
]

    