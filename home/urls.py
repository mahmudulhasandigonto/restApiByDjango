
from django.urls import path
from home import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/brand/', views.brand_list, name='brand_list'),
    path('api/brand/<int:id>', views.brand_details, name='brand_details'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
