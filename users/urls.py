from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('login/', views.login_view, name='login'),
    path('form_registro/', views.signup_view, name='form_registro'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
    path('logout/', views.logout_view, name='logout'),
]