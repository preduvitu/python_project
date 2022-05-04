from django.urls import path
from dashboard.views import (
    dashboard, detalhes
)

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('detalhes/',detalhes, name='detalhes')
]
