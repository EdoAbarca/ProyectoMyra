from django.urls import path
from .views import *
from api import views

urlpatterns=[
    path('profesional/', ProfesionalView.as_view()),
    path('profesional/<int:id>', ProfesionalView.as_view()),
    path('profesional/<str:search>', ProfesionalView.as_view()),
    path('area/', AreaView.as_view()),
    path('area/<int:id>', AreaView.as_view()),
    path('centro/', CentroView.as_view()),
    path('centro/<int:id>', CentroView.as_view()),

    path('cargar_excel/', views.cargar_excel),
    path('register', views.UserRegister.as_view(), name='register'),
	path('login', views.UserLogin.as_view(), name='login'),
	path('logout', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user'),
    
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