from django.urls import path
from .views import *

urlpatterns=[
    path('profesional/', ProfesionalView.as_view()),
    path('profesional/<int:id>', ProfesionalView.as_view())
    
]