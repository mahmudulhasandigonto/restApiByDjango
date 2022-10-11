
from django.urls import path
from home import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/brand/', views.brand, name='brand'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
