from django.urls import path
from django.contrib.auth.decorators import login_required
from accounts.views import (
    login, logout, cadastro
)


urlpatterns = [
    path('', login, name='login'),
    path('account/login/', login, name='login'),
    path('account/logout/', login_required(logout), name='logout'),
    path('account/cadastro/', cadastro, name='cadastro'),
]
