from django.urls import path
from . import views
from .views import get_resort

urlpatterns = [
    path("", views.home, name="home"),
    path('/api/resorts', get_resort, name='get_resort'),
]