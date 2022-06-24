from django.urls import path
from .views import (
    ItemsView
)


app_name = "api_v1"
urlpatterns = [
    path('items/', ItemsView.as_view(), name='items')
]
