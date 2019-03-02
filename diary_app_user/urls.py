from django.urls import path
from . import views

urlpatterns = [
    path('introduce', views.introduce, name = 'introduce'),
    path('<int:daily_id>/', views.detail, name = 'detail'),
    path('new/', views.new, name = 'new'),
    path('create', views.create, name = 'create'),
    path('edit/<int:daily_id>', views.edit, name = 'edit'),
    path('contents', views.contents, name = 'contents'),
    path('logout', views.logout, name = 'logout'),
    path('delete/<int:daily_id>', views.delete, name = 'delete'),
    path('update/<int:daily_id>',views.update, name = 'update'),

]