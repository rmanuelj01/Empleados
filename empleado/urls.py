from django.urls import path
from . import views
from django.contrib.auth.views import logout_then_login, LoginView

urlpatterns = [
    #path('', views.login, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('', LoginView.as_view(template_name = 'login.html'), name='login'),
]