
from django.urls import path
from home import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),
    path('api/brand/', views.brand_list, name='brand_list'),
    path('api/brand/<int:id>', views.brand_details, name='brand_details'),
    path('api/product/', views.product_list, name='product_list'),
    path('api/product/<int:id>', views.product_details, name='product_details'),
    path('api/category/', views.category_list, name='category_list'),
    path('api/category/<int:id>', views.category_details, name='category_details'),
    path('api/news/', views.news_list, name='news_list'),
    path('api/news/<int:id>', views.news_details, name='news_details'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
