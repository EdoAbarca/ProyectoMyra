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
    path('cargo/', CargoView.as_view()),
    path('cargo/<int:id>', CargoView.as_view()),
    path('contrato/', ContratoView.as_view()),
    path('contrato/<int:id>', ContratoView.as_view()),
    path('coordinador/', CoordinadorView.as_view()),
    path('coordinador/<int:id>', CoordinadorView.as_view()),
    path('pago/', PagoView.as_view()),
    path('pago/<int:id>', PagoView.as_view()),
    path('region/', RegionView.as_view()),
    path('region/<int:id>', RegionView.as_view()),
    path('zona/', ZonaView.as_view()),
    path('zona/<int:id>', ZonaView.as_view()),
    path('cliente/', ClienteView.as_view()),
    path('cliente/<int:id>', ClienteView.as_view()),

    path('search-profesional/', SearchView.as_view(), name='search-profesional'),
    path('filter-position/<int:id_area>/', FilterAreaView.as_view(), name='filter-position'),
    path('filter-center/<int:id_centro>/', FilterCenterView.as_view(), name='filter-center'),
    #path('get-profesional/<int:id_profesional>/', MyraView.as_view(), name='get-profesional'),
    path('search-paciente/', SearchPacienteView.as_view(), name='search-paciente'),
    path('filter-client-type/<int:id_cliente>/', FilterTipoClienteView.as_view(), name='filter-client-type'),
    path('filter-turn-type/<int:id_turno>/', FilterTipoTurnoView.as_view(), name='filter-turn-type'),

    path('cargar_excel', views.cargar_excel),
    path('register', views.UserRegister.as_view(), name='register'),
	path('log', views.UserLogin.as_view(), name='login'),
	path('logout', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user'),
    
]
