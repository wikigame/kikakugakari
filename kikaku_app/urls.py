from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('blog/', views.blog, name='blog'),
    path('members/', views.members, name='members'),
    path('contact/', views.contact, name='contact'),
]
