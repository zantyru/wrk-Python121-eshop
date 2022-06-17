from django.urls import path
from item import views

app_name = 'item'
urlpatterns = [
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('categories/<int:category_id>/', views.ItemsInCategoryView.as_view(), name='items_in_category'),
    path('<int:pk>/', views.ItemView.as_view(), name='detail'),
]
