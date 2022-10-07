from django.urls import path
from .views import (
    User,
)

urlpatterns = [
    path('products/', User.as_view(), name="CRUD"),
]