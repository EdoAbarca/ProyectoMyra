from django.urls import path
from .views import *
from api import views

urlpatterns=[
    path('profesional/', ProfesionalView.as_view()),
    path('profesional/<int:id>', ProfesionalView.as_view()),
    path('profesional/<str:search>', ProfesionalView.as_view()),

    path('cargar_excel/', views.cargar_excel),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('signout/', views.signout)
    
]

'''
    path('coordinador/', CoordinadorView.as_view()),
    path('coordinador/<int:id>', CoordinadorView.as_view()),
    path('cargo/', CargoView.as_view()),
    path('cargo/<int:id>', CargoView.as_view()),
    path('pago/', PagoView.as_view()),
    path('pago/<int:id>', PagoView.as_view()),
    path('region/', RegionView.as_view()),
    path('region/<int:id>', RegionView.as_view()),
    path('zona/', ZonaView.as_view()),
    path('zona/<int:id>', ZonaView.as_view()),
    path('cliente/', ClienteView.as_view()),
    path('cliente/<int:id>', ClienteView.as_view()),
    '''