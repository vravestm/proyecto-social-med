from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('inicio_sesion/', views.login_view, name='inicio_sesion'),
    path('form_registro/', views.signup_view, name='form_registro'),
    path('perfil_usuario/', views.perfil_usuario, name='perfil_usuario'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
