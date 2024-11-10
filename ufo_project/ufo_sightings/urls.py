from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
]