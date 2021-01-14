from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('test/', views.test),
]

urlpatterns = format_suffix_patterns(urlpatterns)
