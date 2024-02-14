from django.urls import path
from . import views


urlpatterns = [
    path('',          views.VRegister.as_view(),  name='Authentication'),
    path('logout',    views.logout,               name='Logout'),
    path('login',     views.login,                name='Login'),

    ]